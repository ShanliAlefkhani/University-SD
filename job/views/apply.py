from django.shortcuts import redirect
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from job.models import Job, Application
from job.serializers import ApplicationSerializer


class Apply(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = ApplicationSerializer

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(pk=request.data['job'])
        if timezone.now().date() < job.expire_date:
            submit, created = Application.objects.get_or_create(person=request.user.person, job=job)
            submit.save()
            return Response("Your Application Added Successfully", status=status.HTTP_200_OK)
        return Response("Job was expired", status=status.HTTP_400_BAD_REQUEST)


def apply(request, pk):
    person = request.user.person
    job = Job.objects.get(id=pk)
    Application.objects.create(person=person, job=job)

    return redirect("http://127.0.0.1:8000/job/job-list/")
