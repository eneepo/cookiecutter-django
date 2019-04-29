"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from split_settings.tools import optional, include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/api.py',
    'components/auth.py',
    'components/apps.py',
    'components/asset.py',
    'components/base.py',  # standard django settings
    'components/database.py',  # postgres
    'components/i18n.py',  # postgres
    'components/email.py',
    'components/security.py',
    'components/template.py',

    # Select the right env:
    'environments/%s.py' % ENV,

    optional('environments/temp.py'),
]

# Include settings:
include(*base_settings)
