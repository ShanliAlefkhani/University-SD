from rest_framework import generics

from course.models import Choice
from course.serializers import ChoiceSerializer


class ChoiceDetailView(generics.RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
