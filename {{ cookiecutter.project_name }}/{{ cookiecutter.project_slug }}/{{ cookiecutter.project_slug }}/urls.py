"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ cookiecutter.django_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

{% if cookiecutter.use_oscar == "y" %}
from oscar.app import application
{%- endif %}

{%- if cookiecutter.use_wagtail == "y" %}
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
{%- endif %}

urlpatterns = [
    path('admin/', admin.site.urls),

    {% if cookiecutter.use_wagtail == "y" %}
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),
    {%- endif %}

    {% if cookiecutter.use_oscar == "y" %}
    path('store/', include(application.urls)),
    {%- endif %}

    {%- if cookiecutter.use_wagtail == "y" and cookiecutter.use_oscar == "y" and %}
    url(r'^api/oscar_wagtail/', include('oscar_wagtail.urls')),
    {%- endif %}

]
