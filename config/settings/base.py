"""
Django settings for Artskill project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import oscar

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


def root(*dirs):
    base_dir = os.path.join(os.path.dirname(__file__), '..', '..')
    return os.path.abspath(os.path.join(base_dir, *dirs))


def app_root(*dirs):
    return root('app', *dirs)


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


SITE_NAME = 'Artskill'
SITE_URL = 'http://artskill.store/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'x2cgsvsif8#fzsuv()(w)kt%6p^9+)#wjlwbwdyiyji@df!3=*')

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'wsgi.application'

BASE_DIR = root()

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = app_root('public/static/')
STATICFILES_DIRS = [
    app_root('static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = app_root('public/media/')

LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'widget_tweaks',

    'app.artskill',
    'app.robokassa',
]
# Add forked oscar apps
INSTALLED_APPS = INSTALLED_APPS + oscar.get_core_apps([
    'app.shipping',
    'app.checkout',
    'app.basket',
    'app.catalogue',
    'app.dashboard.catalogue',
    'app.customer',
    'app.partner',
])

# for FlatPages
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            app_root('templates'),
            # app_root('templates/oscar_original'),
            app_root('templates/oscar'),
            # oscar.OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTHENTICATION_BACKENDS = [
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 'PATH': location('whoosh_index'),
    },
}

# Here's a sample Haystack config if using Solr (which is recommended)
# HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8983/solr/',
#        'INCLUDE_SPELLING': True
#    },
# }


# ==============
# Email config
# ==============

EMAIL_SUBJECT_PREFIX = 'Artskill - '
SERVER_EMAIL = 'team@artskill.store'
DEFAULT_FROM_EMAIL = 'team@artskill.store'
OSCAR_FROM_EMAIL = 'team@artskill.store'

# used default
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# or
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''  # !!! PASSWORD


# ==============
# Robokassa config
# ==============

ROBOKASSA_LOGIN = ''
ROBOKASSA_PASSWORD1 = ''
ROBOKASSA_PASSWORD2 = ''

# ROBOKASSA_USE_POST=''
# ROBOKASSA_STRICT_CHECK=''
# ROBOKASSA_TEST_MODE=''
# ROBOKASSA_EXTRA_PARAMS=''
# ROBOKASSA_TEST_FORM_TARGET=''
'''
ROBOKASSA_PASSWORD2 - пароль №2. Его можно не указывать,
                      если django-robokassa используется только для вывода формы платежа.
                      Если django-robokassa используется для приема платежей, то этот параметр обязательный.
ROBOKASSA_USE_POST - используется ли метод POST при приеме результатов от ROBOKASSA.
                     По умолчанию - True. Считается, что для Result URL, Success URL и Fail URL
                     выбран один и тот же метод.
ROBOKASSA_STRICT_CHECK - использовать ли строгую проверку (требовать предварительного уведомления на ResultURL).
                         По умолчанию - True.
ROBOKASSA_TEST_MODE - включен ли тестовый режим.
                      По умолчанию False (т.е. включен боевой режим).
ROBOKASSA_EXTRA_PARAMS - список (list) названий дополнительных параметров,
                         которые будут передаваться вместе с запросами.
                         "Shp" к ним приписывать не нужно.
ROBOKASSA_TEST_FORM_TARGET - url робокассы для тестового режима.
                             Настройка предназначена для случая,
                             когда в распоряжении не имеется доступного в интернете домена
                             (например разработка на localhost) и вместо сервера робокассы
                             необходимо использовать свой.
'''

# ==============
# Oscar settings
# ==============

from oscar.defaults import *

# ====
# Meta
# ====
# OSCAR_USE_LESS = True

OSCAR_SHOP_NAME = 'Artskill'
# OSCAR_SHOP_TAGLINE = 'Tagline'

OSCAR_PROMOTIONS_ENABLED = False
OSCAR_HOMEPAGE = reverse_lazy('artskill:home')

OSCAR_DEFAULT_CURRENCY = 'RUB'
# OSCAR_CURRENCY_FORMAT = {
#     'RUB': {
#         'format': u'#####;',
#     },
# }

# ==============
# Checout processing
# ==============

OSCAR_ALLOW_ANON_CHECKOUT = True
OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'phone_number')

PAYMENT_METHOD_CASH = 'cash'
PAYMENT_METHOD_ROBOKASSA = 'robokassa'

PAYMENT_METHODS = ((PAYMENT_METHOD_ROBOKASSA, 'Оплата на сайте'),
                   (PAYMENT_METHOD_CASH, 'Оплата наличными при получении'))

# ==============
# Order processing
# ================

ORDER_PENDING = 'Ожидает оплаты'
ORDER_PAID = 'Оплачен'
ORDER_ADD_WO_PAY = 'Добавлен, Оплата при получении'

OSCAR_INITIAL_ORDER_STATUS = ORDER_PENDING
OSCAR_INITIAL_LINE_STATUS = 'Добавлен'

# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
    ORDER_PENDING: (ORDER_PAID, 'Выполнен', 'Отмена'),
    ORDER_PAID: ('Выполнен', 'Отмена'),
    ORDER_ADD_WO_PAY: ('Выполнен', 'Отмена'),
    'Выполнен': (),
    'Отмена': (),
}

# ==============
# Oscar Shipping
# ==============

SHIPPING_METHODS_STANDARD_OPTIONS = {
    'standard-take-away': {
        'name': 'Самовывоз',
        'description': ('<p>Товар можете забрать в нашем офисе по адресу:</p>'
                        '<p>СПб, Цветочная, 6M</p>'
                        '<p>Стоимость: бесплатно</p>'
                        '<p>Часы работы: с пн по пт (с 11 до 19:00)</p>'),
    },
    'standard': {
        'name': 'Курьерская по Санкт-Петербургу',
        'description': ('<p>Стоимость: 250 руб<br>'
                        'при заказе от 8000р - бесплатно<br>'
                        'Срок доставки: 1-2 д</p>'
                        '<p>Доставка по Санкт-Петербургу - 250 руб, пригород - 450 руб.<br>'
                        'Быстро и оперативно доставим Вам в течение 1-2 дней.<br>'
                        'Для уточнения свяжитесь с нами: '
                        '<a href="tel:+79215868890" class="header2-menu__phone" title="+7 921 586-88-90">'
                        '+7 921 586-88-90</a>'
                        '</p>'),
        'free_price_from': '8000.00',
        'excl_tax': '250.00',
        'incl_tax': '250.00',
    },
    'boxberry-take-away': {
        'name': 'Пункт выдачи Boxberry',
        'description': ('<p>Доставка до ближайшего к вами пункта выдачи Boxberry</p>'
                        '<p>Стоимость: 350 Р<br>'
                        'при заказе от 5000р - бесплатно<br>'
                        'Срок доставки: 4-5 д</p>'
                        '<p>Пункт выдачи заказов в Вашем городе</p>'
                        '<p>Быстрая курьерская доставка в пункт выдачи заказов, где Вы сможете самостоятельно, '
                        'в удобное для Вас время забрать и оплатить товар Artskill. Все адреса пунктов доступны '
                        'к выбору при оформлении заказа на нашем сайте или на сайте '
                        '<a href="https://boxberry.ru/find_an_office/">https://boxberry.ru/find_an_office/</a></p>'),
        'free_price_from': '5000.00',
        'excl_tax': '350.00',
        'incl_tax': '350.00',
    },
    'boxberry-currier': {
        'name': 'Курьерская доставка Boxberry',
        'description': ('<p>Курьерская доставка Boxberry на дом<br>'
                        'Стоимость: 450 Р<br>'
                        'при заказе от 5000р - бесплатно<br>'
                        'Срок доставки: 4-5 д</p>'),
        'free_price_from': '8000.00',
        'excl_tax': '450.00',
        'incl_tax': '450.00',
    },
    'pochta-russia': {
        'name': 'Почта России',
        'description': ('<p>Классическая доставка почтой России. Вы сможете забрать свою покупку на почте. '
                        'Отправка почтой России осуществляется при 100% оплате у нас на сайте.</p>'
                        '<p>Стоимость: 250 Р<br>'
                        'при заказе от 5000р - бесплатно</p>'),
        'free_price_from': '5000.00',
        'excl_tax': '250.00',
        'incl_tax': '250.00',
    },
}


# ==============
# Oscar Dashboard
# ==============

OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Product Types'),
                'url_name': 'dashboard:catalogue-class-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Orders'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
            # The shipping method dashboard is disabled by default as it might
            # be confusing. Weight-based shipping methods aren't hooked into
            # the shipping repository by default (as it would make
            # customising the repository slightly more difficult).
            # {
            #     'label': _('Shipping charges'),
            #     'url_name': 'dashboard:shipping-method-list',
            # },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customers'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offers'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
            {
                'label': _('Voucher Sets'),
                'url_name': 'dashboard:voucher-set-list',
            },

        ],
    },
    {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]
