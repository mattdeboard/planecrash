from .base import *

DEBUG = TEMPLATE_DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'planecrash',
        'HOST': 'util.local',
        'PORT': '6432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}

INSTALLED_APPS += ('devserver',)
MIDDLEWARE_CLASSES += ('devserver.middleware.DevServerMiddleware',)
DEVSERVER_ARGS = [
    '-6',
    '--wsgi-app=%s/planecrash/wsgi.py' % BASE_DIR,
]
DEVSERVER_MODULES = [
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
]
DEVSERVER_TRUNCATE_SQL = False
STATIC_ROOT = '/home/matt/Envs/planecrash/lib/python2.7/site-packages/django/contrib/admin/static/admin/'
