from django.shortcuts import render, redirect

from job.forms.job import JobForm
from job.models import Job


def job_update(request, pk):
    if request.user.is_anonymous:
        return redirect('http://127.0.0.1:8000/')

    initial_data = {
        'title': Job.objects.get(id=pk).title,
        'description': Job.objects.get(id=pk).description,
        'requirements': Job.objects.get(id=pk).requirements,
        'salary': Job.objects.get(id=pk).salary,
        'work_time': Job.objects.get(id=pk).work_time,
        'location': Job.objects.get(id=pk).location,
        'field': Job.objects.get(id=pk).field,
    }
    job_form = JobForm(request.POST or None, initial=initial_data)

    if job_form.is_valid():
        title = job_form.cleaned_data.get('title')
        description = job_form.cleaned_data.get('description')
        requirements = job_form.cleaned_data.get('requirements')
        salary = job_form.cleaned_data.get('salary')
        work_time = job_form.cleaned_data.get('work_time')
        location = job_form.cleaned_data.get('location')
        field = job_form.cleaned_data.get('field')

        job = Job.objects.get(id=pk)
        job.title = title
        job.description = description
        job.requirements = requirements
        job.salary = salary
        job.work_time = work_time
        job.location = location
        job.field = field
        job.save()

        return redirect("http://127.0.0.1:8000/job/job-detail/")

    context = {
        'job_form': job_form
    }
    return render(request, 'job_update.html', context)
