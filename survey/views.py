from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (
    Quiz,
    Question,
    Choice,
    User_Answer,
    User
)
from .serializers import (
    CreateQuestionSerializer,
    CreateQuizSerializer,
    CreateAnswerSerializer,
    CreateChoiceSerializer,
    GetQuizSerializer,
    GetQuestionSerializer,
    GetUser_AnswerSerializer
)


class QuizViews(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = CreateQuizSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'description')

    def list(self, request, *args, **kwargs):
        queryset = Quiz.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = GetQuizSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = GetQuizSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = CreateQuizSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class QuestionView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('question',)

    def list(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        serializer = GetQuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj


class ChoiceView(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = CreateChoiceSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('text_answer',)


class User_AnswerView(ModelViewSet):
    queryset = User_Answer.objects.all()
    serializer_class = CreateAnswerSerializer


class CetUserAnswerView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUser_AnswerSerializer

    def list(self, request, *args, **kwargs):
        query_set = User_Answer.objects.all()
        serializer = GetUser_AnswerSerializer(query_set,
                                              context={'request': request},
                                              many=True)
        return Response(serializer.data)

