from rest_framework import generics

from job.models import Job
from job.serializers.job import JobSerializer


class JobUpdate(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
