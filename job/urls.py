from django.urls import path

from job.views.job import JobList

urlpatterns = [
    path('job-list/', JobList.as_view()),
]
