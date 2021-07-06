from django.views.generic.detail import DetailView

from course.models import Chapter
from course.serializers import ChapterSerializer


class ChapterDetailView(DetailView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    template_name = "chapter_detail.html"
