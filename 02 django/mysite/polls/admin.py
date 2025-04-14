from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Poll, Question, Choice, Token

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Token)
admin.site.register(Poll)
