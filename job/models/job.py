from django.db import models

from user.models import Company


class Job(models.Model):
    WORK_TIME_CHOICES = (
        ('F', 'Full Time'),
        ('P', 'Part Time'),
        ('R', 'Remote'),
    )
    Field_CHOICES = (
        ('B', 'Back-end'),
        ('F', 'Front-end'),
    )
    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True)
    requirements = models.TextField(max_length=200, null=True)
    salary = models.IntegerField(default=0)
    work_time = models.CharField(max_length=1, choices=WORK_TIME_CHOICES)
    location = models.CharField(max_length=20)
    field = models.CharField(max_length=1, choices=Field_CHOICES)

    @property
    def get_full_field(self):
        if self.field == 'B':
            return 'Back-end'
        return 'Front-end'

    @property
    def get_full_work_time(self):
        if self.work_time == 'F':
            return 'Full Time'
        elif self.work_time == 'P':
            return 'Part Time'
        return 'Remote'

    def __str__(self):
        return self.title + "@" + self.company.name
