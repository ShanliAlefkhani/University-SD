from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course/course-image', null=True)
