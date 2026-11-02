from rest_framework import serializers
from ExamApp.models import QuestionsDb

class QuestionDbSerializer(serializers.Serializer):
    question=serializers.CharField(max_length=200)
    option_a=serializers.CharField(max_length=100)
    option_b=serializers.CharField(max_length=100)
    option_c=serializers.CharField(max_length=100)
    option_d=serializers.CharField(max_length=100)
    correct_answer=serializers.CharField(max_length=200)

class AnswerSubmissionDbSerializer(serializers.Serializer):
    student_name=serializers.CharField(max_length=100)
    question=serializers.IntegerField()
    selected_answer=serializers.CharField(max_length=100)
    submitted_at=serializers.DateTimeField(read_only=True)