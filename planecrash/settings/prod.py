import os.path as osp
from .base import *
BASE_DIR = osp.abspath(osp.join(osp.dirname(osp.dirname(__file__)), '..'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'planecrash',
        'HOST': 'planecrash.c5sy9he6ikco.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
        'USER': 'celeb_pc',
        'PASSWORD': 'b88GIln603Jv'
    }
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'urk0wu4uo@5a#29a2h@@msckvm67)-35hkfeu9q%7t6ijhdye^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'planecrash.urls'

WSGI_APPLICATION = 'planecrash.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = '/opt/Envs/planecrash/lib/python2.7/site-packages/django/contrib/admin/static/admin/'
STATIC_URL = '/static/'
