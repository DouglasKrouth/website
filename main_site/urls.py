from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.home,name="home"),   #empty path for home function
    path("projects/", include("main_site.urls"), name="projects"),
]