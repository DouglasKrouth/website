from django.http import HttpResponse
from django.shortcuts import render
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home_page(request):
    return render(request, "index.html")
    return HttpResponse(html)
