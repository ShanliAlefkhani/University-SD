from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
