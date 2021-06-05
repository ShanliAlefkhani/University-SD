from rest_framework import generics

from course.models import Lesson
from course.serializers import LessonSerializer


class LessonList(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
