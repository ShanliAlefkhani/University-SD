from django.shortcuts import redirect
from django.views.generic import ListView

from job.models import Job
from user.models import Company, Person


class JobList(ListView):
    ordering_fields = ['salary', 'working_hours']
    search_fields = ['title']
    template_name = "job_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('http://127.0.0.1:8000/')
        return super(JobList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        try:
            Company.objects.get(user=self.request.user)
            return Job.objects.filter(company__user=self.request.user)
        except Company.DoesNotExist:
            Person.objects.get(user=self.request.user)
            return Job.objects.all()
