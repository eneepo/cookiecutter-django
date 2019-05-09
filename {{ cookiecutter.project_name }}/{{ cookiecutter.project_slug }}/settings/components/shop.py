{%- if cookiecutter.use_oscar == "y" %}
from oscar.defaults import *

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}
{%- endif %}

{% if cookiecutter.use_wagtail == "y" and cookiecutter.use_oscar == "y" and %}
OSCAR_DASHBOARD_NAVIGATION.insert(1, {
    'label': 'CMS',
    'icon': 'icon-th-list',
    'url_name': 'wagtailadmin_home',
    'access_fn': lambda user, *args: user.has_perm('wagtailadmin.access_admin')
})
{%- endif %}
