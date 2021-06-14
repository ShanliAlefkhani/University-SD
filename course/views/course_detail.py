from rest_framework import generics

from course.models import Course
from course.serializers import CourseSerializer

from django.views.generic.detail import DetailView


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    template_name = "CourseDetail-page/CourseDetails.html"
