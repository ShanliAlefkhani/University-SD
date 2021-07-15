from django.db import models


class BaseCourse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pre_description = models.TextField()
    image = models.ImageField(upload_to='course/course-image', null=True)
