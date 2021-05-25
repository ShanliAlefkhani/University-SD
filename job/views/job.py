from rest_framework import generics

from job.models import Job
from job.serializers.job import JobSerializer


class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    ordering_fields = ['expire_date', 'salary', 'working_hours']
    search_fields = ['title']
