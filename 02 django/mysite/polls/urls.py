from django.urls import path

from mysite.settings import LOGIN_URL

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("answers", views.answers, name="answers"),
    path("poll/<str:id>/", views.poll, name="poll"),
    path("poll/<str:id>/<str:token>/", views.poll_with_token, name="poll_with_token"),
    path(LOGIN_URL, views.login_form, name="login_form"),
    path("poll/<str:id>/save", views.save, name="save"),
    path("login_view", views.login_view, name="login_view"),
    path("dashboard", view=views.dashboard, name="dashboard"),
    path("poll/<str:id>/details", view=views.poll_details, name="poll_details"),
]
