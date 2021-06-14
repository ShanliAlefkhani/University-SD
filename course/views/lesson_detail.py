from django.views.generic.detail import DetailView

from course.models import Lesson
from course.serializers import LessonSerializer


class LessonDetailView(DetailView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    template_name = "lesson_detail_page/Lesson.html"
