from rest_framework import generics

from course.models import Course
from course.serializers import CourseSerializer


class CourseList(generics.ListAPIView):
    queryset = Course
    serializer_class = CourseSerializer
