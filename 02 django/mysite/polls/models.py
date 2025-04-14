from uuid import uuid4
from django.db import models

# Create your models here.

from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid4())


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    poll_id = models.ForeignKey(Poll, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Token(models.Model):
    token = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
