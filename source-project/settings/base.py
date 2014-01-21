# -*- coding: utf-8 -*-

import posixpath

import tempfile, os
from django import contrib
approot = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
adminroot = os.path.join(contrib.__path__[0], 'admin')
tempdata = tempfile.mkdtemp()

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x4$@%buj5c@g6@m(fzhtsv+2z9z88(a0a6_p__yjd)nimv#a)l'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(approot, 'sqlite', '{{ __PROJECT_LABEL__ }}.db'),
        'TEST_NAME': os.path.join(tempdata, '{{ __PROJECT_LABEL__ }}.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

ugettext = lambda s: s # rather hackish but suggested by...
## ... http://docs.djangoproject.com/en/1.1/topics/i18n/deployment/#how-django-discovers-language-preference
## to prevent circular dependancies
LANGUAGES = (
    #('en', ugettext('English')),
    ('de', ugettext('German')),
)

DEFAULT_HTTP_PROTOCOL = 'http'

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(approot, 'face', 'uploaded')

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(approot, 'face', 'static')

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(approot, 'face')
]

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/face/'

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

'''# autoload this templatetags in every template
TEMPLATE_TAGS = ( "uni_form.templatetags.uni_form_tags",
                  "django.templatetags.i18n",
                  "easy_thumbnails.templatetags.thumbnail",
)'''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'ost2.middleware.SubdomainMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware', # DDT
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


# see also:
# http://morethanseven.net/2009/02/10/append-slashes-urls-django.html
# https://docs.djangoproject.com/en/dev/ref/settings/#append-slash
APPEND_SLASH = True

# see also http://shityoucantremember.wordpress.com/2009/02/14/unriddling-the-django-user-profile/
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(approot, 'templates')
)

CONTEXT_SETTINGS = (
    "DEBUG", "MEDIA_URL", "STATIC_URL",
)

CONTEXT_REQUEST_VARS = (
)

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
    'core.context_processors.global_settings',
    'core.context_processors.request_params',
    'core.context_processors.site_url',
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'django.contrib.messages',
    
    #external
    'haystack',
    'gunicorn',
    'django_extensions',
    'test_utils',
    'imagekit',
    'dajaxice',
    'dajax',
    'tagging',
    'south',
    'django_nose',
    'delegate',
    'signalqueue',
)

# Subject-line prefix for e-mail messages sent with django.core.mail.mail_admins or django.core.mail.mail_managers. You'll probably want to include the trailing space.
EMAIL_SUBJECT_PREFIX = u'[Django-Project] '

# The host to use for sending e-mail.
EMAIL_HOST = u'localhost'

# Password to use for the SMTP server defined in EMAIL_HOST. This setting is used in conjunction with EMAIL_HOST_USER when authenticating to the SMTP server. If either of these settings is empty, Django won't attempt authentication.
EMAIL_HOST_PASSWORD = ''
# Username to use for the SMTP server defined in EMAIL_HOST. If empty, Django won't attempt authentication.
EMAIL_HOST_USER = ''

# Port to use for the SMTP server defined in EMAIL_HOST.
EMAIL_PORT = 25
# Whether to use a TLS (secure) connection when talking to the SMTP server.
EMAIL_USE_TLS = False

DAJAXICE_MEDIA_PREFIX = "dajaxice"
DAJAXICE_JSON2_JS_IMPORT = True
DAJAXICE_XMLHTTPREQUEST_JS_IMPORT = True

SQ_QUEUES = {
    'default': {                                            # you need at least one dict named 'default' in IK_QUEUES
        'ENGINE': 'signalqueue.worker.backends.RedisSetQueue',  # required - full path to a QueueBase subclass
        'INTERVAL': 30, # 1/3 sec
        'OPTIONS': dict(),
    },
    'db': {
        'ENGINE': 'signalqueue.worker.backends.DatabaseQueueProxy',
        'INTERVAL': 30, # 1/3 sec
        'OPTIONS': dict(app_label='signalqueue', modl_name='EnqueuedSignal'),
    },
}

SQ_RUNMODE = 'SQ_ASYNC_REQUEST'
SQ_WORKER_PORT = 11231

PIL_IMAGEFILE_MAXBLOCK = 1024 * 2 ** 10
FILE_UPLOAD_MAX_MEMORY_SIZE = 33554432

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    }
}

HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr'
HAYSTACK_LIMIT_TO_REGISTERED_MODELS = False

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
