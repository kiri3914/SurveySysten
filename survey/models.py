from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField

User = get_user_model()


class Quiz(models.Model):
    """
    Атрибуты опроса:
    название, дата старта,
    дата окончания, описание.
    """
    title = models.CharField(max_length=255, verbose_name='Название опроса')
    date_start = models.DateTimeField(verbose_name='Дата начала')
    date_end = models.DateTimeField(verbose_name='Дата оканчания')
    description = models.TextField(verbose_name='Описание')
    slug = AutoSlugField(populate_from='title', default=None, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['-date_start']


class Question(models.Model):
    """
    Атрибуты вопросов:
    текст вопроса, тип вопроса
    """

    question = models.CharField(max_length=500, verbose_name='Текст вопроса')
    type = models.CharField(
        choices=(
            ('TEXT', 'text'),
            ('ONE', 'one'),
            ('MANY', 'many')
        ),
        max_length=255,
        verbose_name='тип вопроса'
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Опрос', related_name='question_quiz')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['question']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choice')
    text_answer = models.TextField()
    is_right = models.BooleanField(default=False)


class User_Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answer')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='user_choice', blank=True, null=True)

    text_answer = models.TextField(blank=True, null=True)
