from .base import *


DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'uber',
#         'HOST': 'localhost',
#     }
# }

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE


# =============
# Debug Toolbar
# =============

INTERNAL_IPS = ['127.0.0.1', '::1']

#### Sentry
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn="https://9e2e031ae09b4f95b8e232b0376e7ff1@sentry.io/1401064",
#     integrations=[DjangoIntegration()]
# )

# sentry_sdk.capture_message('Test Sentry!', level='info')