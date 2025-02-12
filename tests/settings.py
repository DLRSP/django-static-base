"""Test's settings"""

import os

from django.utils.translation import gettext_noop

DEBUG = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

SECRET_KEY = "NOTASECRET"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "static_base",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [os.path.join(BASE_DIR, "templates")],
    }
]

ROOT_URLCONF = "tests.urls"

MIDDLEWARE = (
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
)

USE_TZ = True
LANGUAGE_CODE = "en"
USE_I18N = True

STATIC_URL = "/static/"

# Languages we provide translations for, out of the box.
LANGUAGES = [
    ("de", gettext_noop("German")),
    ("en", gettext_noop("English")),
    ("es", gettext_noop("Spanish")),
    ("fr", gettext_noop("French")),
    ("it", gettext_noop("Italian")),
    ("ja", gettext_noop("Japanese")),
    ("nl", gettext_noop("Dutch")),
    ("ru", gettext_noop("Russian")),
    ("zh-hans", gettext_noop("Simplified Chinese")),
    ("zh-hant", gettext_noop("Traditional Chinese")),
]
