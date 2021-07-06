from django.views.generic.detail import DetailView

from course.models import Course
from course.serializers import CourseSerializer


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    template_name = "course_detail.html"
