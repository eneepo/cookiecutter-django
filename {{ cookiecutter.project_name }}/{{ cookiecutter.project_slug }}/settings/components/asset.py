import os
from os.path import dirname, abspath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets/'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django imagekit configuration
# https://django-imagekit.readthedocs.io/en/latest/configuration.html
IMAGEKIT_CACHEFILE_DIR = 'cache/images'
