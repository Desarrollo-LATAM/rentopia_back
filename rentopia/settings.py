"""
Django settings for rentopia project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import logging
import os
from datetime import timedelta
from pathlib import Path

import environ

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
print("E U R E K A -- BASE_DIR: " + os.path.join(BASE_DIR, ".env"))

# False if not in os.environ because of casting above
DEBUG = env("DEBUG")
print(" RED PILL:", DEBUG)

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

ALLOWED_HOSTS = []


# Application definition
# Applications core of Django
BASE_APPS = [   
    "daphne",     
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Local applications
LOCAL_APPS = [
    "apps.users",
    "apps.booking",
    "apps.chatbot",
    "apps.geolocalization",
    "apps.messaging",
    "apps.properties",
    "apps.rating",
    "apps.upload",
    "apps.owners",
    "apps.tenants",
    "apps.authentication",
]

# Third persons applications
THIRD_APPS = [      
    "channels", 
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "django_filters",
    "drf_spectacular",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    #"allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "drf_standardized_errors",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #"allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "rentopia.urls"

SITE_ID = 1  # make sure SITE_ID is set

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "rentopia.wsgi.application"

ASGI_APPLICATION = "rentopia.asgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

<<<<<<< HEAD
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'real_state',
        'USER': 'postgres',
        'PASSWORD': 'Kurama331',
        'HOST': 'localhost',  # Puedes cambiarlo si tu base de datos está en otro host
        'PORT': '5432',  # El puerto predeterminado de PostgreSQL es 5432
    }
}
=======
>>>>>>> origin/back_silvina

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Buenos_Aires"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "complexsigningkey",  # generate a key and replace me
    "ALGORITHM": "HS512",
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
    "REGISTER_SERIALIZER": "apps.users.api.serializers.UserRegistrationSerializer",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Rentopia API",
    "DESCRIPTION": "API para la plataforma de alquiler de propiedades Rentopia",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
    "COMPONENT_SPLIT_REQUEST": True,
    # "SCHEMA_PATH_PREFIX_INSERT": "/staging",
    # OTHER SETTINGS
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.choices",
        "ClientErrorEnum": "drf_standardized_errors.openapi_serializers.ClientErrorEnum.choices",
        "ServerErrorEnum": "drf_standardized_errors.openapi_serializers.ServerErrorEnum.choices",
        "ErrorCode401Enum": "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.choices",
        "ErrorCode403Enum": "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.choices",
        "ErrorCode404Enum": "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.choices",
        "ErrorCode405Enum": "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.choices",
        "ErrorCode406Enum": "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.choices",
        "ErrorCode415Enum": "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.choices",
        "ErrorCode429Enum": "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.choices",
        "ErrorCode500Enum": "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.choices",
    },
    "POSTPROCESSING_HOOKS": [
        "drf_standardized_errors.openapi_hooks.postprocess_schema_enums"
    ],
}

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         "APP": {"client_id": "123", "secret": "456", "key": ""}
#     }
# }

ACCOUNT_AUTHENTICATION_METHOD = "username"
# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup. When set to
# "mandatory" the user is blocked from logging in until the email
# address is verified. Choose "optional" or "none" to allow logins
# with an unverified e-mail address. In case of "optional", the e-mail
# verification mail is still sent, whereas in case of "none" no e-mail
# verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# <EMAIL_CONFIRM_REDIRECT_BASE_URL>/<key>
EMAIL_CONFIRM_REDIRECT_BASE_URL = "http://localhost:3000/email/confirm/"

# <PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL>/<uidb64>/<token>/
PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL = (
    "http://localhost:3000/password-reset/confirm/"
)

STATIC_URL = "staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URLS = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# # Correo electrónico
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ADMINS = [({env("ADMIN1_NAME")}, {env("ADMIN1_EMAIL")})]

# Logging
PROPAGATE = env("PROPAGATE")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": "DEBUG",
        # Adding the watchtower handler here causes all loggers in the project that
        # have propagate=True (the default) to send messages to watchtower. If you
        # wish to send only from specific loggers instead, remove "watchtower" here
        # and configure individual loggers below.
        "handlers": ["console"],
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        # "console": {
        #     "class": "logging.StreamHandler",
        # },
    },
    "loggers": {
        # In the debug server (`manage.py runserver`), several Django system loggers cause
        # deadlocks when using threading in the logging handler, and are not supported by
        # watchtower. This limitation does not apply when running on production WSGI servers
        # (gunicorn, uwsgi, etc.), so we recommend that you set `propagate=True` below in your
        # production-specific Django settings file to receive Django system logs in CloudWatch.
        # "django": {
        #     "level": "DEBUG",
        #     "handlers": ["console"],
        #     "propagate": PROPAGATE,
        # }
        # Add any other logger-specific configuration here.
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            "propagate": PROPAGATE,
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": PROPAGATE,
        },
    },
}
