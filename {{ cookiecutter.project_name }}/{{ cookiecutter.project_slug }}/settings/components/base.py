"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django {{ cookiecutter.django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/ref/settings/
"""
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    {%- if cookiecutter.use_wagtail == "y" %}
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    {%- endif %}
]

ROOT_URLCONF = '{{ cookiecutter.project_slug }}.urls'

SITE_ID = 1

WSGI_APPLICATION = '{{ cookiecutter.project_slug }}.wsgi.application'
