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

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]