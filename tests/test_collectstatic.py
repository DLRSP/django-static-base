"""collectstatic integration: package assets land under STATIC_ROOT (S1)."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from django.core.management import call_command
from django.test import SimpleTestCase, override_settings

from tests.test_static_finders import COLOR_THEMES, MATERIAL_ASSETS

REQUIRED_ASSETS = (
    "base/css/bootstrap.min.css",
    "base/js/jquery.min.js",
    "base/js/bootstrap.bundle.min.js",
    "base/css/bootstrap.css",
    "base/js/bootstrap.min.js",
)

_STATICFILES_STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    },
}


class CollectstaticIntegrationTests(SimpleTestCase):
    def _collect(self, tmp: str) -> Path:
        with override_settings(
            STATIC_ROOT=tmp,
            STORAGES=_STATICFILES_STORAGES,
        ):
            call_command(
                "collectstatic",
                interactive=False,
                verbosity=0,
                clear=True,
            )
        return Path(tmp).resolve()

    def test_collectstatic_copies_required_assets(self):
        tmp = tempfile.mkdtemp(prefix="static_base_collect_")
        try:
            root = self._collect(tmp)
            for name in REQUIRED_ASSETS:
                dest = (root / name).resolve()
                self.assertTrue(dest.is_file(), f"missing after collectstatic: {name}")
                self.assertTrue(
                    str(dest).startswith(str(root)),
                    f"path escaped STATIC_ROOT: {dest}",
                )
                self.assertGreater(dest.stat().st_size, 0, name)
                self.assertIn(dest.suffix, {".css", ".js"}, name)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_collectstatic_color_themes_under_static_root(self):
        """S1: color theme CSS lands under STATIC_ROOT with no path escape."""
        tmp = tempfile.mkdtemp(prefix="static_base_themes_")
        try:
            root = self._collect(tmp)
            for theme in COLOR_THEMES:
                name = f"base/css/color/{theme}.css"
                dest = (root / name).resolve()
                self.assertTrue(dest.is_file(), f"missing theme after collectstatic: {name}")
                self.assertTrue(
                    str(dest).startswith(str(root)),
                    f"theme path escaped STATIC_ROOT: {dest}",
                )
                self.assertGreater(dest.stat().st_size, 0, name)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_collectstatic_material_dashboard_under_static_root(self):
        """Material Dashboard theme + companions land under STATIC_ROOT."""
        tmp = tempfile.mkdtemp(prefix="static_base_material_")
        try:
            root = self._collect(tmp)
            for name in MATERIAL_ASSETS:
                dest = (root / name).resolve()
                self.assertTrue(
                    dest.is_file(), f"missing Material after collectstatic: {name}"
                )
                self.assertTrue(
                    str(dest).startswith(str(root)),
                    f"Material path escaped STATIC_ROOT: {dest}",
                )
                self.assertGreater(dest.stat().st_size, 0, name)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_collectstatic_clear_idempotent(self):
        tmp = tempfile.mkdtemp(prefix="static_base_idem_")
        try:
            root = self._collect(tmp)
            first_size = (root / "base/js/jquery.min.js").stat().st_size
            root = self._collect(tmp)
            second = root / "base/js/jquery.min.js"
            self.assertTrue(second.is_file())
            self.assertEqual(second.stat().st_size, first_size)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
