from .base import *

# ALLOWED_HOSTS = ['artskill.store']
ALLOWED_HOSTS = ['artskill.store', '46.17.45.249', 'localhost', '127.0.0.1']

STATIC_ROOT = '/artskill/static/'
MEDIA_ROOT = '/artskill/media/'

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'artskilldb',
        'USER': 'artskill',
        'PASSWORD': 'artskillpassw',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}
'''


# ==============
# Email config
# ==============

ADMINS = [('Artskill', 'artskillstore@gmail.com'), ('Team', 'team@artskill.store'), ]

EMAIL_SUBJECT_PREFIX = 'Artskill - '
SERVER_EMAIL = 'team@artskill.store'
DEFAULT_FROM_EMAIL = 'team@artskill.store'
OSCAR_FROM_EMAIL = 'team@artskill.store'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = 'team@artskill.store'
EMAIL_HOST_PASSWORD = 'deadsister1'