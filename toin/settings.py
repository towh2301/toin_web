import os
from pathlib import Path
import mimetypes
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-b!vgt!q$z-k9rwxagd4kv_wqn=dai_uqv1!$5y1!iyzjzaix=i"
)
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

_default_allowed_hosts = [
    "127.0.0.1",
    "localhost",
    "192.168.61.147",
    "toin.onrender.com",
]
_env_allowed_hosts = os.getenv("ALLOWED_HOSTS", "")
if _env_allowed_hosts:
    ALLOWED_HOSTS = [h.strip() for h in _env_allowed_hosts.split(",") if h.strip()]
else:
    ALLOWED_HOSTS = _default_allowed_hosts
if DEBUG and "*" not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append("*")

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "anymail",
    "pages",
    "converter",
]

# Add MIME types
mimetypes.add_type("application/font-woff", ".woff", True)
mimetypes.add_type("font/woff2", ".woff2", True)
mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("application/javascript", ".js", True)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "toin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "toin.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# If DATABASE_URL is provided (e.g., by Render), override default database
_db_config = dj_database_url.config(conn_max_age=600, ssl_require=not DEBUG)
if _db_config:
    DATABASES["default"] = _db_config

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "vi"
USE_I18N = True
USE_L10N = True
TIME_ZONE = "UTC"
USE_TZ = True

LANGUAGES = [("en", "English"), ("vi", "Vietnamese"), ("jp", "Japanese")]
LOCALE_PATHS = [BASE_DIR / "locale"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Trust the proxy (Render) and enforce HTTPS in production
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = not DEBUG

# CSRF trusted origins (from env or derived from allowed hosts)
_env_csrf = os.getenv("CSRF_TRUSTED_ORIGINS", "")
if _env_csrf:
    CSRF_TRUSTED_ORIGINS = [o.strip() for o in _env_csrf.split(",") if o.strip()]
else:
    CSRF_TRUSTED_ORIGINS = []
    for host in ALLOWED_HOSTS:
        if host in {"127.0.0.1", "localhost"} or host.startswith("192.168."):
            CSRF_TRUSTED_ORIGINS.append(f"http://{host}")
            CSRF_TRUSTED_ORIGINS.append(f"https://{host}")
        elif host and host != "*":
            CSRF_TRUSTED_ORIGINS.append(f"https://{host}")

"""
Email Configuration
-------------------
We avoid SMTP on Render by using HTTP API providers via django-anymail.
Supported providers: sendgrid, resend. Fallbacks: console (dev) or SMTP (legacy).

Environment variables:
  EMAIL_PROVIDER=sendgrid|resend   # choose API provider (optional). If set, used in all envs.
  DEFAULT_FROM_EMAIL=...           # required for all email scenarios

  # For SendGrid
  SENDGRID_API_KEY=...

  # For Resend
  RESEND_API_KEY=...

  # Legacy SMTP fallback (only used if EMAIL_PROVIDER not set)
  EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD,
  EMAIL_USE_TLS, EMAIL_USE_SSL

  # Optional
  ANYMAIL_DEBUG=true|false         # log request/response
  FORCE_SMTP=true                  # force SMTP even in DEBUG (not recommended on Render)
"""

EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER", "").strip().lower()
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "tuyendung@toin.com.vn")
DEFAULT_TO_EMAIL = os.getenv("DEFAULT_TO_EMAIL", "h_huy@toin-vn.com")

if EMAIL_PROVIDER in {"sendgrid", "resend"}:
    # Configure django-anymail for HTTP API sending
    ANYMAIL = {
        "DEBUG_API_REQUESTS": os.getenv("ANYMAIL_DEBUG", "false").lower() == "true",
    }
    if EMAIL_PROVIDER == "sendgrid":
        ANYMAIL["SENDGRID_API_KEY"] = os.getenv("SENDGRID_API_KEY", "")
        EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
    elif EMAIL_PROVIDER == "resend":
        ANYMAIL["RESEND_API_KEY"] = os.getenv("RESEND_API_KEY", "")
        EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"

    # Basic validation to avoid silent misconfigurations in production
    if not DEBUG:
        api_key = (
            ANYMAIL.get("SENDGRID_API_KEY")
            if EMAIL_PROVIDER == "sendgrid"
            else ANYMAIL.get("RESEND_API_KEY")
        )
        if not api_key:
            print(
                "⚠️ WARNING: EMAIL_PROVIDER is set to",
                EMAIL_PROVIDER,
                "but the corresponding API key env var is missing. Falling back to console backend.",
            )
            EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

elif DEBUG and os.getenv("FORCE_SMTP", "").lower() != "true":
    # Development default: use console backend (outputs to stdout/logs)
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    # Legacy SMTP (kept for backwards compatibility or when explicitly required)
    EMAIL_BACKEND = os.getenv(
        "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
    )
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "true").lower() == "true"
    EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "false").lower() == "true"
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

    # Safety fallback: gracefully degrade if credentials are missing in production
    if not DEBUG and (not EMAIL_HOST_USER or not EMAIL_HOST_PASSWORD):
        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
        print(
            "⚠️ WARNING: Missing SMTP credentials (EMAIL_HOST_USER or EMAIL_HOST_PASSWORD). "
            "Using console backend instead. Configure EMAIL_PROVIDER and API key to avoid SMTP on Render."
        )

# Error Page Handlers
# Custom error views with styled templates using header and footer
# These provide branded 404 and 500 error pages instead of Django defaults
handler404 = "pages.views.page_not_found"  # 404 - Page not found
handler500 = "pages.views.server_error"  # 500 - Server error
