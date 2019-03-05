from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']

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


# ==============
# Email config
# ==============

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SERVER_EMAIL = 'smurov@yandex.ru'
DEFAULT_FROM_EMAIL = 'smurov@yandex.ru'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'smurov'
EMAIL_HOST_PASSWORD = 'igor'  # !!! PASSWORD

# ==============
# Robokassa config
# ==============

'''
team_team
admin
p762W3Q4b9
'''

ROBOKASSA_TEST_MODE = True

ROBOKASSA_LOGIN = 'test_site_team'
ROBOKASSA_PASSWORD1 = 'CehVFetX13NQ68SeRJw2'
ROBOKASSA_PASSWORD2 = 'KWtl3Wa81B9X8xvIPBFj'

#### Sentry
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn="https://9e2e031ae09b4f95b8e232b0376e7ff1@sentry.io/1401064",
#     integrations=[DjangoIntegration()]
# )

# sentry_sdk.capture_message('Test Sentry!', level='info')
