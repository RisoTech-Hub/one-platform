"""
Base settings to build other settings files upon.
"""
from pathlib import Path

import environ
from django.utils.translation import gettext_lazy as _

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# one/
APPS_DIR = ROOT_DIR / "one"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".envs/.local/.django"))
    env.read_env(str(ROOT_DIR / ".envs/.local/.postgres"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Ho_Chi_Minh"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
VIETNAMESE = "vi"
ENGLISH = "en"
LANGUAGES = [
    (VIETNAMESE, _("Vietnamese")),
    (ENGLISH, _("English")),
]
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
# SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",  # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
EXTENDED_APPS = [
    "one.contrib.auth.contexts",
    "one.contrib.contenttypes.configs",
    "one.contrib.sites.settings",
    "one.extend.riso_allauth",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
    "webpush",
    "django_filters",
    "filebrowser",
    "tinymce",
]
LOCAL_APPS = [
    "one.components",
    "one.users",
    # CORE
    "one.core.menu",
    "one.core.dynamic",
    # CMS
    "one.cms.home",
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + EXTENDED_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {
    "auth": "one.contrib.auth.migrations",
    "contenttypes": "one.contrib.contenttypes.migrations",
    "sites": "one.contrib.sites.migrations",
}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "one.users.middleware.ActiveUserMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"
# https://django-filebrowser.readthedocs.io/en/latest/settings.html#settings
FILEBROWSER_DIRECTORY = ""
DIRECTORY = ""

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "one.extend.metronic.context_processors.layout_context",
                "one.extend.riso_allauth.context_processors.allauth_settings",
                "one.contrib.sites.settings.context_processors.site_setting_processor",
            ],
            "builtins": [
                "django.templatetags.i18n",
                "django.templatetags.static",
                "one.extend.metronic.templatetags.theme",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""Bin Nguyen""", "support@example.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-extended
CELERY_RESULT_EXTENDED = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-send-task-events
CELERY_WORKER_SEND_TASK_EVENTS = True
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_send_sent_event
CELERY_TASK_SEND_SENT_EVENT = True
# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "one.extend.riso_allauth.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
ACCOUNT_FORMS = {"signup": "one.extend.riso_allauth.forms.UserSignupForm"}
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "one.extend.riso_allauth.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
SOCIALACCOUNT_FORMS = {"signup": "one.extend.riso_allauth.forms.UserSocialSignupForm"}

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework_datatables.renderers.DatatablesRenderer",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework_datatables.filters.DatatablesFilterBackend",
    ),
    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework_datatables.pagination.DatatablesPageNumberPagination"
    ),
    "PAGE_SIZE": 50,
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"

# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "Riso Tech one platform API",
    "DESCRIPTION": "Documentation of API endpoints of Riso Tech one platform",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVERS": [
        {"url": "http://127.0.0.1:8000", "description": "Local Development server"},
        {"url": "https://example.com", "description": "Production server"},
    ],
}

# Web push notification
# ------------------------------------------------------------------------------
WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": env("VAPID_PUBLIC_KEY", default=""),
    "VAPID_PRIVATE_KEY": env("VAPID_PRIVATE_KEY", default=""),
    "VAPID_ADMIN_EMAIL": env("VAPID_ADMIN_EMAIL", default=""),
}

# User active
# ------------------------------------------------------------------------------
# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 300

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LAST_SEEN_TIMEOUT = 60 * 60 * 24 * 7

# METRONIC SETTINGS
# ------------------------------------------------------------------------------

# Theme name
KT_THEME = "metronic"

# Theme layout templates directory
KT_THEME_LAYOUT_DIR = "layout"

# Theme Mode
KT_THEME_MODE_DEFAULT = "light"  # Value: light | dark | system
KT_THEME_MODE_SWITCH_ENABLED = True

# Theme Direction
KT_THEME_DIRECTION = "ltr"  # Value: ltr | rtl

# Theme Assets
KT_THEME_ASSETS = {
    "favicon": "media/logos/favicon.ico",
    "fonts": [
        "https://fonts.googleapis.com/css?family=Inter:300,400,500,600,700",
    ],
    "css": ["plugins/global/plugins.bundle.css", "css/style.bundle.css"],
    "js": ["plugins/global/plugins.bundle.js", "js/scripts.bundle.js"],
}

# Theme Vendors
KT_THEME_VENDORS = {
    "datatables": {
        "css": ["plugins/custom/datatables/datatables.bundle.css"],
        "js": ["plugins/custom/datatables/datatables.bundle.js"],
    },
    "formrepeater": {"js": ["plugins/custom/formrepeater/formrepeater.bundle.js"]},
    "fullcalendar": {
        "css": ["plugins/custom/fullcalendar/fullcalendar.bundle.css"],
        "js": ["plugins/custom/fullcalendar/fullcalendar.bundle.js"],
    },
    "flotcharts": {"js": ["plugins/custom/flotcharts/flotcharts.bundle.js"]},
    "google-jsapi": {"js": ["//www.google.com/jsapi"]},
    "tinymce": {"js": ["plugins/custom/tinymce/tinymce.bundle.js"]},
    "ckeditor-classic": {"js": ["plugins/custom/ckeditor/ckeditor-classic.bundle.js"]},
    "ckeditor-inline": {"js": ["plugins/custom/ckeditor/ckeditor-inline.bundle.js"]},
    "ckeditor-balloon": {"js": ["plugins/custom/ckeditor/ckeditor-balloon.bundle.js"]},
    "ckeditor-balloon-block": {
        "js": ["plugins/custom/ckeditor/ckeditor-balloon-block.bundle.js"]
    },
    "ckeditor-document": {
        "js": ["plugins/custom/ckeditor/ckeditor-document.bundle.js"]
    },
    "draggable": {"js": ["plugins/custom/draggable/draggable.bundle.js"]},
    "fslightbox": {"js": ["plugins/custom/fslightbox/fslightbox.bundle.js"]},
    "jkanban": {
        "css": ["plugins/custom/jkanban/jkanban.bundle.css"],
        "js": ["plugins/custom/jkanban/jkanban.bundle.js"],
    },
    "typedjs": {"js": ["plugins/custom/typedjs/typedjs.bundle.js"]},
    "cookiealert": {
        "css": ["plugins/custom/cookiealert/cookiealert.bundle.css"],
        "js": ["plugins/custom/cookiealert/cookiealert.bundle.js"],
    },
    "cropper": {
        "css": ["plugins/custom/cropper/cropper.bundle.css"],
        "js": ["plugins/custom/cropper/cropper.bundle.js"],
    },
    "vis-timeline": {
        "css": ["plugins/custom/vis-timeline/vis-timeline.bundle.css"],
        "js": ["plugins/custom/vis-timeline/vis-timeline.bundle.js"],
    },
    "jstree": {
        "css": ["plugins/custom/jstree/jstree.bundle.css"],
        "js": ["plugins/custom/jstree/jstree.bundle.js"],
    },
    "prismjs": {
        "css": ["plugins/custom/prismjs/prismjs.bundle.css"],
        "js": ["plugins/custom/prismjs/prismjs.bundle.js"],
    },
    "leaflet": {
        "css": ["plugins/custom/leaflet/leaflet.bundle.css"],
        "js": ["plugins/custom/leaflet/leaflet.bundle.js"],
    },
    "amcharts": {
        "js": [
            "https://cdn.amcharts.com/lib/5/index.js",
            "https://cdn.amcharts.com/lib/5/xy.js",
            "https://cdn.amcharts.com/lib/5/percent.js",
            "https://cdn.amcharts.com/lib/5/radar.js",
            "https://cdn.amcharts.com/lib/5/themes/Animated.js",
        ]
    },
    "amcharts-maps": {
        "js": [
            "https://cdn.amcharts.com/lib/5/index.js",
            "https://cdn.amcharts.com/lib/5/map.js",
            "https://cdn.amcharts.com/lib/5/geodata/worldLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/continentsLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/usaLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/worldTimeZonesLow.js",
            "https://cdn.amcharts.com/lib/5/geodata/worldTimeZoneAreasLow.js",
            "https://cdn.amcharts.com/lib/5/themes/Animated.js",
        ]
    },
    "amcharts-stock": {
        "js": [
            "https://cdn.amcharts.com/lib/5/index.js",
            "https://cdn.amcharts.com/lib/5/xy.js",
            "https://cdn.amcharts.com/lib/5/themes/Animated.js",
        ]
    },
    "bootstrap-select": {
        "css": ["plugins/custom/bootstrap-select/bootstrap-select.bundle.css"],
        "js": ["plugins/custom/bootstrap-select/bootstrap-select.bundle.js"],
    },
}

# Custom libraries
KT_CUSTOM_LIBS = {
    # Metronic Reinit libs always placed at top of this list
    "metronic": {"js": ["js/metronic/init.js"]},
    "filebrowser": {
        "css": ["filebrowser/css/filebrowser.css"],
        "js": ["filebrowser/js/fileuploader.js", "js/filebrowser/upload_button.js"],
    },
    "webpush": {
        "js": ["js/webpush/auto.js"],
    },
    "widget": {
        "js": [
            "js/widgets/model_select_actions.js",
            "js/widgets/table_multiple_formset.js",
            "js/utilities.js",
        ],
    },
    # Custom JS always placed at the end of this list
    "project": {
        "css": ["css/project.css"],
        "js": ["js/project.js"],
    },
}

# Django TinyMCE
# ------------------------------------------------------------------------------
TINYMCE_JS_URL = STATIC_URL + KT_THEME_VENDORS["tinymce"]["js"][0]
TINYMCE_JS_ROOT = STATIC_URL + "plugins/custom/tinymce"
TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}

# Your stuff...
# ------------------------------------------------------------------------------
