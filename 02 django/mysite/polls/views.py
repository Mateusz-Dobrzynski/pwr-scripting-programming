from django.shortcuts import render
from .models import Question
from .models import Choice
from .models import Token
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def answers(request):
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/answers.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def poll(request):
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/poll.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def poll_with_token(request, token):
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/poll.html")
    context = {
        "latest_question_list": latest_question_list,
        "token": token,
    }
    print(f"token: {token}")
    return HttpResponse(template.render(context, request))


def save(request):
    token = request.GET.get("token", None)
    if token:
        try:
            correspondingToken = Token.objects.get(token=token)
            return HttpResponse("You are not allowed to vote again")
        except Exception as e:
            print("bajojajo", e)
            for item in request.GET:
                if item != "csrfmiddlewaretoken" and item != "token":
                    selected_choice = Choice.objects.get(choice_text=request.GET[item])
                    selected_choice.votes += 1
                    selected_choice.save()
            used_token = Token()
            used_token.token = token
            used_token.save()
            return HttpResponse("Answers saved!")
