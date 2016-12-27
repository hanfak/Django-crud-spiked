from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.all()
    context = { 'latest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)

def show(request, question_id):
    a_question = __get_question(question_id)
    all_choices = a_question.choice_set.all()
    context = {
        'a_question': a_question,
        'all_choices': all_choices,
    }
    return render(request, 'polls/show.html', context)

def new(request):
    return render(request, 'polls/new.html')

def create(request):
    new_question = Question(question_text=request.POST['question_text'])
    new_question.save()
    return redirect('/polls/')

def edit(request, question_id):
    a_question = __get_question(question_id)
    context = { 'question': a_question }
    return render(request, 'polls/edit.html', context)

def update(request, question_id):
    edited_question = __get_question(question_id)
    edited_question.question_text = request.POST['question_text']
    edited_question.save()
    return redirect('/polls/')

def destroy(request, question_id):
    a_question = __get_question(question_id)
    a_question.delete()
    return redirect('/polls/')

def __get_question(question_id):
    return get_object_or_404(Question, pk = question_id)
