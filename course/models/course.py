from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='course/course-image', null=True)
