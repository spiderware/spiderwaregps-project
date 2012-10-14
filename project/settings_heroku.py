"""
Collects as much information as possible from ENV for auto-configuration.
Individual items should actually be exported from here and integrated into heroku-buildpack-python
"""
from .settings import *
import os
def sentry_config(default='', env='SENTRY_DSN'):
    """alter settings from SENTRY_DSN."""
    return os.environ.get(env, default)

def debug_config(default=True, env='DJANGO_DEBUG'):
    return bool(int(os.environ.get(env, default)))

def aws_access_key_id_config(default=None, env='AWS_ACCESS_KEY_ID'):
    return os.environ.get(env, default)

def aws_secret_access_key_config(default=None, env='AWS_SECRET_ACCESS_KEY'):
    return os.environ.get(env, default)

def aws_default_storage_bucket_name_config(default=None, env='AWS_DEFAULT_STORAGE_BUCKET_NAME'):
    return os.environ.get(env, default)

DEBUG = debug_config(default=DEBUG)
SENTRY_DSN = sentry_config(default=locals().get('SENTRY_DSN'))

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

AWS_ACCESS_KEY_ID = aws_access_key_id_config()
AWS_SECRET_ACCESS_KEY = aws_secret_access_key_config()
AWS_STORAGE_BUCKET_NAME = aws_default_storage_bucket_name_config()

# storage and media
DEFAULT_FILE_STORAGE = 'project.storage_backends.MediaStorage'
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# cache (using the memcachier addon)
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': os.environ.get('MEMCACHIER_SERVERS', ''),
        'TIMEOUT': 500,
        'BINARY': True,
        }
}

# general google analytics
ANALYTICAL_AUTO_IDENTIFY = False
GOOGLE_ANALYTICS_SITE_SPEED = True
GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID', None)

# gaug.es
GAUGES_SITE_ID = os.environ.get('GAUGES_SITE_ID', None)

# security and ssl related settings (django-secure)
SECURE_SSL_REDIRECT = bool(os.environ.get('SECURE_SSL_REDIRECT', False))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', 0))
SECURE_HSTS_INCLUDE_SUBDOMAINS = bool(os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', False))
SESSION_COOKIE_SECURE = SECURE_SSL_REDIRECT
SESSION_COOKIE_HTTPONLY = SECURE_SSL_REDIRECT