from django.db import models

from user.models import Company


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    expire_date = models.DateField()
    salary = models.IntegerField(default=0)
    working_hours = models.IntegerField()

    def __str__(self):
        return self.title + "@" + self.company.name
