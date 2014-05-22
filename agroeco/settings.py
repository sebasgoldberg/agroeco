"""
Django settings for agroeco project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


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
    ] + get_core_apps()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.middleware.transaction.TransactionMiddleware',  # Django 1.5 only
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'agroeco.urls'

WSGI_APPLICATION = 'agroeco.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS': True,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-AR'

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
  #location('templates'),
  OSCAR_MAIN_TEMPLATE_DIR,
  )

from oscar.defaults import *

HAYSTACK_CONNECTIONS = {
  'default': {
  'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
  },
}

STATIC_ROOT = '%s/static' % BASE_DIR
COMPRESS_ROOT = STATIC_ROOT
