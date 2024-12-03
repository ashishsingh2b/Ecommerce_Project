from django.views import generic
from django.http import HttpResponse

def myname(request):
    return HttpResponse("Hello, world!")