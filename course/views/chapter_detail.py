from rest_framework import generics

from course.models import Chapter
from course.serializers import ChapterSerializer


class ChapterDetailView(generics.RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
