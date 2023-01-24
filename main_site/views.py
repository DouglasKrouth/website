from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    return render(request, "base_generic.html")

def projects(request):
     template = loader.get_template('projects.html')
     context = {}
     return HttpResponse(template.render(context, request))

def about_page(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))

def projects_page(request):
    template = loader.get_template('projects.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contact_page(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))
