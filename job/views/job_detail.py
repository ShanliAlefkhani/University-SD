from django.views.generic import DetailView

from job.models import Job
from job.serializers.job import JobSerializer


class JobDetail(DetailView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    template_name = 'job_detail.html'
