"""krouth_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main_site.views import current_datetime, home, projects
from django.conf.urls import include
from django.urls import path, re_path

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    # Index/homepage
    path(r"", home, name="home"),
    path(r"index", home, name="home"),
    path(r"projects", projects, name="projects"),
]

# Add static urls to site pattern
urlpatterns += staticfiles_urlpatterns()
