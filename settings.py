ADMINS = (
	('Match Strike', 'info@matchstrike.net'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SITE_NAME='HAPPO'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# List of all installed authentication backends
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

# List of template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'context_processors.default',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'south',
	'compress',
	'champion_manager',
	'gunicorn',
	'sentry.client'
)

# Login configuration
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

# E-mail config
EMAIL_SUBJECT_PREFIX = '[%s] ' % (SITE_NAME,)
DEFAULT_FROM_EMAIL = 'info@matchstrike.net'
SEND_BROKEN_LINK_EMAILS = False

# djanog-compress settings.
COMPRESS_CSS = {
	'main': {
		'source_filenames': (
			'css/happo.css',
		),
		'output_filename': 'css/happo.r?.css',
    },
}

COMPRESS_JS = {
	'main': {
		'source_filenames': (
			'js/googleAnalytics.js',
			'js/form.js',
			'js/happo.js',
		),
		'output_filename': 'js/happo.r?.js',
	},
}

# Import local settings.
try:
    from local_settings import *
except ImportError:
    pass