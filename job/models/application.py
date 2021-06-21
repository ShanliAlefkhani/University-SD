from django.db import models

from job.models import Job
from user.models import Person


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
