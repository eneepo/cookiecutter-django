# Application definition
{%- if cookiecutter.use_oscar == "y" %}
from oscar import get_core_apps
{%- endif %}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    {% if cookiecutter.use_wagtail == "y" %}
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    {%- endif %}

    {%- if cookiecutter.use_wagtail == "y" and cookiecutter.use_oscar == "y" and %}
    'oscar_wagtail',
    {%- endif %}
]

{%- if cookiecutter.use_oscar == "y" %}
 + get_core_apps()
{%- endif %}
