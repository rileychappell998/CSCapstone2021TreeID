import os

ALLOWED_HOSTS = []
DEBUG = True
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
ROOT_URLCONF="mysite.urls"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/media/'