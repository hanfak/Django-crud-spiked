from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello Everyone")

def root_page(request):
    return HttpResponse("Root page")

def diff_path(request, number=10):
    rand_num = random.randrange(0, int(number))
    message = "random number is " + str(rand_num) + "\npassed in number " + str(number)
    return HttpResponse(message)

def query(request):
    x = request.GET.get('input', '')
    return HttpResponse("the number is " + x )
