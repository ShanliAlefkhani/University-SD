from django.views.generic.list import ListView

from course.models import Course
from course.serializers import CourseSerializer


class CourseList(ListView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    template_name = "course_list_page/course_list.html"
