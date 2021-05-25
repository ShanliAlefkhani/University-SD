from rest_framework import generics
from django.views.generic.list import ListView
from course.models import Question
from course.serializers import QuestionSerializer


class QuestionList(ListView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    template_name = 'Question-Page/Question-List.html'
