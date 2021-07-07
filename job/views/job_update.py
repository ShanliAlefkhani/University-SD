from django.shortcuts import render

from job.forms.job_create import JobForm
from job.models import Job
from user.models import Company


def job_update(request):
    initial_data = {
        'title': Job.objects.get(user=request.user).title,
        'description': Job.objects.get(user=request.user).description,
        'requirements': Job.objects.get(user=request.user).requirements,
        'salary': Job.objects.get(user=request.user).salary,
        'work_time': Job.objects.get(user=request.user).work_time,
    }
    job_form = JobForm(request.POST or None, initial=initial_data)

    if job_form.is_valid():
        title = job_form.cleaned_data.get('title')
        description = job_form.cleaned_data.get('description')
        requirements = job_form.cleaned_data.get('requirements')
        salary = job_form.cleaned_data.get('salary')
        work_time = job_form.cleaned_data.get('work_time')

        company = Company.objects.get(user=request.user)

        Job.objects.update(
            company=company,
            title=title,
            description=description,
            requirements=requirements,
            salary=salary,
            work_time=work_time,
        )

        # return redirect("http://127.0.0.1:8000/user/login/")

    context = {
        'job_form': job_form
    }
    return render(request, 'job_update.html', context)
