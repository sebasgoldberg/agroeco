# coding=utf-8
"""
Django settings for agroeco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from ambiente import ambiente
AMBIENTE=ambiente

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
location = lambda x: os.path.join(
  os.path.dirname(os.path.dirname(__file__)), x)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '37$imvpca^w=qg22f%c^da^9rvmx*!8sw-&82*2!@1o^x(_)i9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

from oscar import get_core_apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'south',
    'compressor',
    'iampacks.cross.install',
    ] + get_core_apps([
      'shipping',
      'basket',
      ])

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    #'django.middleware.transaction.TransactionMiddleware',  # Django 1.5 only
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'agroeco.urls'

WSGI_APPLICATION = 'agroeco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': ambiente.db.name,                      # Or path to database file if using sqlite3.
        'USER': ambiente.db.user,                      # Not used with sqlite3.
        'PASSWORD': ambiente.db.password,                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'TEST_CHARSET': 'utf8',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-AR'
#LANGUAGE_CODE = 'en-US'

gettext = lambda s: s

LANGUAGES = (
  #('en-US', gettext('English')),
  ('es-AR', gettext('Spanish')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.request",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.tz",
  "django.contrib.messages.context_processors.messages",
  'oscar.apps.search.context_processors.search_form',
  'oscar.apps.promotions.context_processors.promotions',
  'oscar.apps.checkout.context_processors.checkout',
  'oscar.apps.customer.notifications.context_processors.notifications',
  'oscar.core.context_processors.metadata',
  )

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
  'oscar.apps.customer.auth_backends.Emailbackend',
  'django.contrib.auth.backends.ModelBackend',
  )

from oscar import OSCAR_MAIN_TEMPLATE_DIR

TEMPLATE_DIRS = (
  OSCAR_MAIN_TEMPLATE_DIR,
  location('templates'),
  )

from oscar.defaults import *

HAYSTACK_CONNECTIONS = {
  'default': {
  'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
  },
}

STATIC_ROOT = location('public/static')
COMPRESS_ROOT = STATIC_ROOT

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = OSCAR_INITIAL_ORDER_STATUS
OSCAR_ORDER_STATUS_PIPELINE = {
  'Pending': ('Being processed', 'Cancelled', ),
  'Being processed': ('Processed', 'Cancelled',),
  'Processed': (),
  'Cancelled': (),
}
OSCAR_LINE_STATUS_PIPELINE = OSCAR_ORDER_STATUS_PIPELINE

MEDIA_URL = '/media/'
#MEDIA_ROOT = '%s/media' % BASE_DIR
MEDIA_ROOT = location("public/media")

OSCAR_SHOP_NAME = 'Productor Agroecológico'
OSCAR_DEFAULT_CURRENCY = '$'
OSCAR_FROM_EMAIL = ambiente.email.user
OSCAR_ALLOW_ANON_CHECKOUT = False
OSCAR_ALLOW_ANON_REVIEWS = False
OSCAR_MODERATE_REVIEWS = True
