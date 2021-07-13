from django.shortcuts import render, redirect
from rest_framework import generics

from job.forms.job import JobForm
from job.models import Job
from job.serializers.job import JobSerializer
from user.models import Company


class JobCreate(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


def job_create(request):
    if request.user.is_anonymous:
        return redirect('http://127.0.0.1:8000/')

    initial_data = {
        'description': 'We are looking for a ...'
    }
    job_form = JobForm(request.POST or None, initial=initial_data)

    if job_form.is_valid():
        title = job_form.cleaned_data.get('title')
        description = job_form.cleaned_data.get('description')
        requirements = job_form.cleaned_data.get('requirements')
        salary = job_form.cleaned_data.get('salary')
        work_time = job_form.cleaned_data.get('work_time')

        company = Company.objects.get(user=request.user)

        Job.objects.create(
            company=company,
            title=title,
            description=description,
            requirements=requirements,
            salary=salary,
            work_time=work_time,
        )

        return redirect("http://127.0.0.1:8000/job/job-list/")

    context = {
        'job_form': job_form
    }
    return render(request, 'job_create.html', context)
