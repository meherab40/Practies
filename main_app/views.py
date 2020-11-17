from django.http import HttpResponse
from django.http import request

def homeView(request):
    return HttpResponse("Hello World")