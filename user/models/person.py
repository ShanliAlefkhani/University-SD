from django.contrib.auth.models import User
from django.db import models

from course.models.course import Course


class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, related_name='person', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    birthday = models.DateField('birthday')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    github_id = models.CharField(max_length=100, default='-')
    linkedin_id = models.CharField(max_length=100, default='-')
    courses = models.ManyToManyField(Course, related_name='persons')

    class Meta:
        ordering = ['name']

    @property
    def effective_username(self):
        return self.user.username

    @property
    def get_first_course(self):
        return self.courses.first()
