from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.home,name="home"),   #empty path for home function
    path("projects/", views.projects_page, name="projects"),
    path("about/", views.about_page, name="about"),
    path("contact/", views.contact, name="contact")
]