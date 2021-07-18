from django.views.generic.detail import DetailView

from course.models import BaseCourse
from course.serializers import CourseSerializer


class CourseDetailView(DetailView):
    queryset = BaseCourse.objects.all()
    serializer_class = CourseSerializer
    template_name = "course_detail.html"
