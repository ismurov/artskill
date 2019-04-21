import os
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

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': True,
# }

# ==============
# Email config
# ==============

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = [('Team', 'team@artskill.store'), ]

OWNER_EMAIL = 'owner@artskill.store'

SERVER_EMAIL = 'team@artskill.store'
DEFAULT_FROM_EMAIL = 'team@artskill.store'
OSCAR_FROM_EMAIL = 'team@artskill.store'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# ==============
# Robokassa config
# ==============

'''
team_team
admin
p762W3Q4b9
'''

ROBOKASSA_TEST_MODE = True

ROBOKASSA_LOGIN = os.getenv('ROBOKASSA_LOGIN', 'test_site_team')
ROBOKASSA_PASSWORD1 = os.getenv('ROBOKASSA_PASSWORD1', 'CehVFetX13NQ68SeRJw2')
ROBOKASSA_PASSWORD2 = os.getenv('ROBOKASSA_PASSWORD2', 'KWtl3Wa81B9X8xvIPBFj')
