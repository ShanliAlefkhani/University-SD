from django import forms

from job.models import Job


class JobForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(),
        label='Job Title:',
    )

    description = forms.CharField(
        widget=forms.Textarea(),
        label='Job Description:',
    )

    requirements = forms.CharField(
        widget=forms.Textarea(),
        label='Requirements(Please write each one in a separate line!):',
    )

    salary = forms.IntegerField(
        widget=forms.TextInput(),
        label='Salary(Please write it in Toman!):',
    )

    work_time = forms.CharField(
        widget=forms.Select(choices=Job.WORK_TIME_CHOICES),
        label='Work Time(Full Time / Part Time / Remote):',
    )
