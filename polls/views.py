from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    context = { 'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)

def show(request, question_id):
    a_question = get_object_or_404(Question, pk = question_id)
    all_choices = a_question.choice_set.all()
    context = {
        'a_question': a_question,
        'all_choices': all_choices,
    }
    return render(request, 'polls/show.html', context)
