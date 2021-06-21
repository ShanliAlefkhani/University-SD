from rest_framework import generics

from job.models import Application
from job.serializers import ApplicationListSerializer


class ApplicationList(generics.ListAPIView):
    serializer_class = ApplicationListSerializer

    def get_queryset(self):
        return Application.objects.filter(job__company=self.request.user.company)
