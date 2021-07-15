from django.views.generic.list import ListView

from course.models import BaseCourse
from course.serializers import CourseSerializer


class CourseList(ListView):
    queryset = BaseCourse.objects.all()
    serializer_class = CourseSerializer
    template_name = "course_list.html"
