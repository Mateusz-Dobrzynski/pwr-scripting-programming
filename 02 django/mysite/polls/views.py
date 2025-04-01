from django.shortcuts import render
from .models import Question
from .models import Choice
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def answers(request):
    latest_question_list = Question.objects.all()
    template = loader.get_template('polls/answers.html')
    context = {
    'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))   

def poll(request):
    latest_question_list = Question.objects.all()
    template = loader.get_template('polls/poll.html')
    context = {
    'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def save(request):
    if request.method == 'GET':
        for item in request.GET:
            if item != "csrfmiddlewaretoken":
                selected_choice = Choice.objects.get(choice_text=request.GET[item])
                selected_choice.votes += 1
                selected_choice.save()
    return HttpResponse("Answers saved!")
