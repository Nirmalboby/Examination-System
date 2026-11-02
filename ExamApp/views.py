from django.shortcuts import render, get_object_or_404
from ExamApp.models import QuestionsDb,AnswerSubmissionDb
from ExamApp.serializers import QuestionDbSerializer,AnswerSubmissionDbSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class QuestionListCreateView(APIView):

    # Retrieve all questions
    def get(self, request):
        qs = QuestionsDb.objects.all()
        serializer_instance = QuestionDbSerializer(qs, many=True)
        return Response(serializer_instance.data)

    # Create a question
    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionDbSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            qs = QuestionsDb.objects.create(**actual_data)

            return Response(QuestionDbSerializer(qs).data)

        else:
            return Response(serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(APIView):

    #  Retrieve one question
    def get(self, request, pk):
        #qs = QuestionsDb.objects.get(id=pk)
        qs=get_object_or_404(QuestionsDb, id=pk)
        serializer_instance = QuestionDbSerializer(qs)
        return Response(serializer_instance.data)

    #  Update a question
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = QuestionDbSerializer(data=form_data)

        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data

            QuestionsDb.objects.filter(id=pk).update(**actual_data)

            qs = QuestionsDb.objects.get(id=pk)
            return Response(QuestionDbSerializer(qs).data)

        else:
            return Response(serializer_instance.errors)

    # Delete a question
    def delete(self, request, pk):
        QuestionsDb.objects.filter(id=pk).delete()
        return Response({
            "message": "Question deleted successfully"
        })

class AnswerSubmissionListCreateView(APIView):
    def get(self, request):
        qs=AnswerSubmissionDb.objects.all()
        serializer_instance=AnswerSubmissionDbSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data=request.data
        serializer_instance=AnswerSubmissionDbSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            AnswerSubmissionDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

