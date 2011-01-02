import logging
import os

from sentry.client.handlers import SentryHandler

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# E-mail config
if DEBUG:
	EMAIL_PORT = 1025

# Cache settings
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_SECONDS = 55*60
CACHE_MIDDLEWARE_KEY_PREFIX = 'happo-matchstrike-net'
	
if DEBUG == True:
	CACHE_BACKEND = 'dummy:///'

# Location of project directory.
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/assets/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Primary templates directory.
TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates'),)

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'happo.db',						# Or path to database file if using sqlite3.
		'USER': '',						 # Not used with sqlite3.
		'PASSWORD': '',					 # Not used with sqlite3.
		'HOST': '',						 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',						 # Set to empty string for default. Not used with sqlite3.
	}
}

# Logging Configuration
logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
	filename = os.path.join(SITE_ROOT, 'happo.log'),
	filemode = 'a',
)

# djanog-compress settings.
# Insert link or script tags for compressed JS/CSS files - must run ./manage.py synccompress
# If false, this inserts the uncompressed version. Use this in development.
COMPRESS = True

# Add version strings to compressed files
COMPRESS_VERSION = True

# Automatically generate new compressed JS and CSS files without running synccompress - only use this in DEV
COMPRESS_AUTO = DEBUG

# Django Sentry
SENTRY_REMOTE_URL = 'https://xxxxxxxxxx/sentry/store/'
SENTRY_KEY = 'xxxxxxxxxxxx'

logger = logging.getLogger()
# ensure we havent already registered the handler
if SentryHandler not in map(lambda x: x.__class__, logger.handlers):
	logger.addHandler(SentryHandler())

	# Add StreamHandler to sentry's default so you can catch missed exceptions
	logger = logging.getLogger('sentry.errors')
	logger.propagate = False
	logger.addHandler(logging.StreamHandler())