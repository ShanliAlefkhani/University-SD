from django.db import models

from user.models import Company


class Job(models.Model):
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    requirements = models.CharField(max_length=200, null=True)
    salary = models.IntegerField(default=0)
    working_hours = models.IntegerField()

    def __str__(self):
        return self.title + "@" + self.company.name
