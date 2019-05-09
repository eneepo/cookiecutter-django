{%- if cookiecutter.use_wagtail == "y" %}
# https://docs.wagtail.io/en/v2.5.1/advanced_topics/settings.html
WAGTAIL_SITE_NAME = '{{ cookiecutter.project_name }}'
WAGTAIL_APPEND_SLASH = True

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = '{{ cookiecutter.email }}'
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
WAGTAILADMIN_NOTIFICATION_INCLUDE_SUPERUSERS = False
{%- endif %}
