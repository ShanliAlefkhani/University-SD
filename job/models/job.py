from django.db import models

from user.models import Company


class Job(models.Model):
    WORK_TIME_CHOICES = (
        ('F', 'Full Time'),
        ('P', 'Part Time'),
        ('R', 'Remote'),
    )
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)
    requirements = models.TextField(max_length=200, null=True)
    salary = models.IntegerField(default=0)
    work_time = models.CharField(max_length=1, choices=WORK_TIME_CHOICES)

    def __str__(self):
        return self.title + "@" + self.company.name
