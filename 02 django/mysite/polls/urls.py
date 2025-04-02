from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("answers", views.answers, name="answers"),
    path("poll", views.poll, name="poll"),
    path("poll/<str:token>/", views.poll_with_token, name="poll_with_token"),
    path("save", views.save, name="save"),
]
