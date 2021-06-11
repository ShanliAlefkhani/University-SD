from rest_framework import generics

from course.models import Lesson
from course.serializers import LessonSerializer


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
