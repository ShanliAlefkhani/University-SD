from rest_framework import generics

from course.models import Chapter
from course.serializers import ChapterSerializer


class ChapterList(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
