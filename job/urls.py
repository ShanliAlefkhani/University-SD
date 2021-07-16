from django.urls import path
from job.views import JobList, Apply, ApplicationList, job_create, job_update, JobDetail

urlpatterns = [
    path('job-list/', JobList.as_view()),
    path('job-create/', job_create),
    path('job-detail/<pk>/', JobDetail.as_view()),
    path('job-update/<pk>/', job_update),
    path('apply/', Apply.as_view()),
    path('job-applications/<pk>/', ApplicationList.as_view()),
]
