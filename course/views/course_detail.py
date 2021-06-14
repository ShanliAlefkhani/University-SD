from rest_framework import generics

from course.models import Course
from course.serializers import CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    template_name = "CourseDetail-Page/CourseDetails.html"