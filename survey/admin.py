from django.contrib.admin import ModelAdmin, register
from .models import Quiz, Question, User_Answer, Choice


@register(Quiz)
class QuestionAdmin(ModelAdmin):
    list_display = ('title', 'date_start', 'date_end', 'slug')


@register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('question', 'type', 'quiz')


@register(Choice)
class QuestionAdmin(ModelAdmin):
    list_display = ('question', 'text_answer', 'is_right')


@register(User_Answer)
class QuestionAdmin(ModelAdmin):
    list_display = ('user', 'question', 'choice', 'text_answer')
