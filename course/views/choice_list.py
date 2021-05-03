from rest_framework import generics

from course.models import Choice
from course.serializers import ChoiceSerializer


class ChoiceList(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
