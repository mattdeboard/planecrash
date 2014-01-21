import os.path as osp
BASE_DIR = osp.abspath(osp.join(osp.dirname(osp.dirname(__file__)), '..'))
SECRET_KEY = 'urk0wu4uo@5a#29a2h@@msckvm67)-35hkfeu9q%7t6ijhdye^'
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = [
    'chrome-extension://knjakhddgpokehcmdjgjpoognlfjiono',
    '.newsblur.com'
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fuselage',
    'tastypie',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'planecrash.urls'

WSGI_APPLICATION = 'planecrash.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
