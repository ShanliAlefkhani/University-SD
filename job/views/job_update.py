from rest_framework import generics

from job.models import Job
from job.serializers import JobUpdateSerializer


class JobUpdate(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobUpdateSerializer
