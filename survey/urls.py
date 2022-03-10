from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    QuizViews,
    ChoiceView,
    QuestionView,
    User_AnswerView,
    CetUserAnswerView
)

router = DefaultRouter()
router.register('quiz', QuizViews, basename='Quiz')
router.register('choice', ChoiceView, basename='Choice')
router.register('user_answer', User_AnswerView, basename='User_answer')
router.register('question', QuestionView, basename='Question')
router.register('get_user_answer', CetUserAnswerView, basename='Get_user_answer')

urlpatterns = []
urlpatterns += router.urls
