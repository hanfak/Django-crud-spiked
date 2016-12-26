from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("details %s" % question_id)
