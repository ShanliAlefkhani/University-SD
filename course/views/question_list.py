from rest_framework import generics

from course.models import Question
from course.serializers import QuestionSerializer


class QuestionList(generics.ListAPIView):
    queryset = Question
    serializer_class = QuestionSerializer
