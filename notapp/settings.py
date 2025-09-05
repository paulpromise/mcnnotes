# Redirect to custom login view
LOGIN_URL = '/login/'

"""
Django settings for notapp project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-keep-it-safe'  # Replace with a secure key in production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Temporarily set to True to see detailed errors

ALLOWED_HOSTS = [
    "mcleansnote-g2ghfaddc3f3c4b9.eastus-01.azurewebsites.net",
    "note.mcleanstech.com",
    "*",  # for testing, tighten later
]

# CSRF Settings
CSRF_TRUSTED_ORIGINS = [
    "https://mcleansnote-g2ghfaddc3f3c4b9.eastus-01.azurewebsites.net",
    "http://mcleansnote-g2ghfaddc3f3c4b9.eastus-01.azurewebsites.net",  # Allow both HTTP and HTTPS
    "https://note.mcleanstech.com",
    "http://note.mcleanstech.com"  # Allow both HTTP and HTTPS
]

# Security Settings
CSRF_COOKIE_SECURE = False  # Set to False temporarily to debug
SESSION_COOKIE_SECURE = False  # Set to False temporarily to debug
SECURE_SSL_REDIRECT = False  # Allow both HTTP and HTTPS for now

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "notes",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",  # Add default CSRF middleware
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "notapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "notes" / "templates", BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "notapp.wsgi.application"

# Database
# Default to SQLite, but use PostgreSQL if DATABASE_URL is set (Azure production)
if os.getenv("DATABASE_URL"):
    import dj_database_url

    DATABASES = {
        "default": dj_database_url.parse(os.getenv("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 9}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "notes" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Session settings
SESSION_COOKIE_AGE = 3600  # 1 hour
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Django Axes (login security) – optional
AXES_FAILURE_LIMIT = 5
AXES_LOCKOUT_TIMEOUT = 30
AXES_USE_USER_AGENT = True
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "ERROR"),
        },
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"