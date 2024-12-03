from django.views import generic
from django.http import HttpResponse

def myname(request):
    return HttpResponse("Hello, world!")

def admindashboard(request):
    return HttpResponse("Welcome to Admin Dashboard")
def userdahsboard(request):
    return HttpResponse("Welcome to User Dashboard")
