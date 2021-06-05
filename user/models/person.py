from django.contrib.auth.models import User
from django.db import models

from course.models import Course


class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    user = models.OneToOneField(User, related_name='person', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    birthday = models.DateField('birthday')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    github_id = models.CharField(max_length=100, null=True)
    linkedin_id = models.CharField(max_length=100, null=True)
    courses = models.ManyToManyField(Course, related_name='persons')

    class Meta:
        ordering = ['name']
