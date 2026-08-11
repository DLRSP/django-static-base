"""Integration tests: package static assets are discoverable by Django finders."""

from pathlib import Path

from django.contrib.staticfiles import finders
from django.test import SimpleTestCase

COLOR_THEMES = (
    "aqua",
    "blue",
    "brown",
    "forest",
    "green",
    "ice",
    "navy",
    "oasis",
    "orange",
    "pink",
    "purple",
    "red",
    "salmon",
    "sky",
    "teal",
    "yellow",
)


# Creative Tim Material Dashboard (+ companions used by DLRSP blog/dashboard shells).
# Paths mirror Bootstrap: theme CSS/JS at base/{css,js}/; helpers under base/js/plugins/.
MATERIAL_ASSETS = (
    "base/css/material-dashboard.css",
    "base/js/material.min.js",
    "base/js/material-dashboard.js",
    "base/js/plugins/chartist.min.js",
    "base/js/plugins/bootstrap-notify.js",
)


class StaticBaseFinderTests(SimpleTestCase):
    """Wheel/package must expose base CSS/JS under static/base/."""

    REQUIRED_ASSETS = (
        "base/css/bootstrap.min.css",
        "base/js/jquery.min.js",
        "base/js/bootstrap.bundle.min.js",
        "base/css/bootstrap.css",
        "base/js/bootstrap.min.js",
    )

    def test_required_assets_are_findable(self):
        missing = [name for name in self.REQUIRED_ASSETS if finders.find(name) is None]
        self.assertEqual(missing, [], f"static_base missing assets: {missing}")

    def test_found_paths_exist_on_disk(self):
        for name in self.REQUIRED_ASSETS:
            path = finders.find(name)
            self.assertIsNotNone(path, name)
            self.assertTrue(Path(path).is_file(), path)

    def test_required_assets_nonempty_and_extension(self):
        for name in self.REQUIRED_ASSETS:
            path = finders.find(name)
            self.assertIsNotNone(path, name)
            file_path = Path(path)
            self.assertGreater(file_path.stat().st_size, 0, name)
            expected_suffix = Path(name).suffix
            self.assertEqual(file_path.suffix, expected_suffix, name)
            self.assertIn(expected_suffix, {".css", ".js"}, name)

    def test_color_themes_findable(self):
        """All packaged color theme CSS files are discoverable."""
        missing = []
        for theme in COLOR_THEMES:
            name = f"base/css/color/{theme}.css"
            path = finders.find(name)
            if path is None or not Path(path).is_file():
                missing.append(name)
                continue
            self.assertGreater(Path(path).stat().st_size, 0, name)
            self.assertEqual(Path(path).suffix, ".css", name)
        self.assertEqual(missing, [], f"missing color themes: {missing}")

    def test_jquery_and_bootstrap_content_markers(self):
        jquery = Path(finders.find("base/js/jquery.min.js"))
        bundle = Path(finders.find("base/js/bootstrap.bundle.min.js"))
        self.assertIn("jQuery", jquery.read_text(encoding="utf-8", errors="replace"))
        self.assertIn(
            "Bootstrap", bundle.read_text(encoding="utf-8", errors="replace")
        )

    def test_material_dashboard_assets_findable(self):
        missing = [name for name in MATERIAL_ASSETS if finders.find(name) is None]
        self.assertEqual(missing, [], f"static_base missing Material assets: {missing}")
        for name in MATERIAL_ASSETS:
            path = Path(finders.find(name))
            self.assertTrue(path.is_file(), name)
            self.assertGreater(path.stat().st_size, 0, name)
            self.assertIn(path.suffix, {".css", ".js"}, name)

    def test_material_dashboard_content_markers(self):
        css = Path(finders.find("base/css/material-dashboard.css"))
        md_js = Path(finders.find("base/js/material-dashboard.js"))
        material = Path(finders.find("base/js/material.min.js"))
        chartist = Path(finders.find("base/js/plugins/chartist.min.js"))
        self.assertIn(
            "Material Dashboard", css.read_text(encoding="utf-8", errors="replace")
        )
        self.assertIn(
            "Material Dashboard", md_js.read_text(encoding="utf-8", errors="replace")
        )
        self.assertIn("ripples", material.read_text(encoding="utf-8", errors="replace"))
        self.assertIn("Chartist", chartist.read_text(encoding="utf-8", errors="replace"))

    def test_app_is_installed(self):
        from django.apps import apps

        self.assertTrue(apps.is_installed("static_base"))
