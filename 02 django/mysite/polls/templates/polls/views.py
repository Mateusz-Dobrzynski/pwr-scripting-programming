from django.shortcuts import redirect, render

from mysite.settings import LOGIN_URL

from .models import Question
from .models import Choice
from .models import Token
from django.template import loader
from django.contrib.auth import authenticate, login

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
    if not request.user.is_authenticated:
        return redirect(f"{LOGIN_URL}?next={request.path}")
    latest_question_list = Question.objects.all()
    template = loader.get_template("polls/poll.html")
    context = {"latest_question_list": latest_question_list, "next": request.path}
    return HttpResponse(template.render(context, request))


def login_form(request):
    template = loader.get_template("polls/login.html")
    return HttpResponse(template.render({"next": request.GET["next"]}, request))


def login_view(request):
    username = request.POST["login"]
    password = request.POST["password"]
    next = request.POST["next"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return redirect(next)
    else:
        template = loader.get_template("polls/error.html")
        return HttpResponse(template.render({}, request))


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
            for item in request.GET:
                if item != "csrfmiddlewaretoken" and item != "token":
                    selected_choice = Choice.objects.get(choice_text=request.GET[item])
                    selected_choice.votes += 1
                    selected_choice.save()
            used_token = Token()
            used_token.token = token
            used_token.save()
            return HttpResponse("Answers saved!")
