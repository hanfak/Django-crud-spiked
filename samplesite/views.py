from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello Everyone")

def root_page(request):
    return HttpResponse("Root page")
