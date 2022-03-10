from rest_framework import serializers
from .models import (
    Quiz,
    Question,
    Choice,
    User_Answer,
    User
)


class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'date_start', 'date_end', 'description', 'slug')
        extra_kwargs = {
            'slug': {'read_only': True},
        }


class CreateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Answer
        fields = "__all__"


class CreateQuestionSerializer(serializers.ModelSerializer):
    # user_answer = CreateAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"


class CreateChoiceSerializer(serializers.ModelSerializer):
    question_choice = CreateQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Choice
        fields = "__all__"


class GetQuizSerializer(serializers.ModelSerializer):
    question_quiz = CreateQuestionSerializer(many=True, read_only=True)

    # answer = CreateAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = "__all__"


class GetQuestionSerializer(serializers.ModelSerializer):
    question_choice = CreateChoiceSerializer(read_only=True, many=True)
    answer = CreateAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = "__all__"


class GetUser_AnswerSerializer(serializers.ModelSerializer):
    user_answer = CreateAnswerSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('username', 'user_answer')

        extra_kwargs = {
            'username': {'read_only': True},
            'user_answer': {'read_only': True},
        }

    # def get_value(self, user_id, quiz_id):
    #     total = User_Answer.objects.filter(
    #         question__quiz=quiz_id,
    #         user_id=user_id,
    #         choice__is_right=True).count()
    #     return total
