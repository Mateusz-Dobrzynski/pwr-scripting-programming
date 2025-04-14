from django.shortcuts import redirect, render

from mysite.settings import LOGIN_URL

from .models import Poll, Question
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


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect(f"{LOGIN_URL}?next={request.path}")
    polls = Poll.objects.all()
    context = {"polls": polls}
    template = loader.get_template("polls/dashboard.html")
    return HttpResponse(template.render(context, request))


def poll_details(request, id):
    if not request.user.is_authenticated:
        return redirect(f"{LOGIN_URL}?next={request.path}")
    questions = Question.objects.filter(poll_id=id)
    context = {"questions": []}
    for question in questions:
        question_context = {"text": question.question_text, "choices": []}
        choices = Choice.objects.filter(question=question)
        for choice in choices:
            question_context["choices"].append(choice)
        context["questions"].append(question_context)
    template = loader.get_template("polls/details.html")
    return HttpResponse(template.render(context, request))


def poll(request, id):
    if not request.user.is_authenticated:
        return redirect(f"{LOGIN_URL}?next={request.path}")
    questions_list = Question.objects.filter(poll_id=id)
    template = loader.get_template("polls/poll.html")
    context = {"questions_list": questions_list, "id": id}
    return HttpResponse(template.render(context, request))


def login_form(request):
    template = loader.get_template("polls/login.html")
    return HttpResponse(template.render({"next": request.GET["next"]}, request))


def login_view(request):
    username = request.POST["login"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request.POST["next"])
    else:
        template = loader.get_template("polls/error.html")
        return HttpResponse(template.render({}, request))


def poll_with_token(request, id, token):
    questions_list = Question.objects.all()
    template = loader.get_template("polls/poll.html")
    context = {
        "questions_list": questions_list,
        "token": token,
        "id": id,
    }
    return HttpResponse(template.render(context, request))


def save(request, id):
    token_in_request: Token = request.GET.get("token", None)
    current_poll = Poll.objects.get(id=id)
    if token_in_request:
        print(token_in_request)
        try:
            correspondingToken = Token.objects.get(
                token=token_in_request, poll=current_poll
            )
            return HttpResponse("You are not allowed to vote again")
        except Exception as e:
            handle_non_token_items(request)
            token_to_save = Token()
            token_to_save.token = token_in_request
            token_to_save.poll = current_poll
            token_to_save.save()
            return HttpResponse("Answers saved!")
    else:
        handle_non_token_items(request)
        return HttpResponse("Answers saved!")


def handle_non_token_items(request):
    for item in request.GET:
        if item != "csrfmiddlewaretoken" and item != "token":
            selected_choice = Choice.objects.get(choice_text=request.GET[item])
            selected_choice.votes += 1
            selected_choice.save()
