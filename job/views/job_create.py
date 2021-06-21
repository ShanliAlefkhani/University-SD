from rest_framework import generics

from job.models import Job
from job.serializers.job import JobSerializer


class JobCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
