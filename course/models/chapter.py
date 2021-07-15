from django.db import models

from course.models.base_course import BaseCourse


class Chapter(models.Model):
    course = models.ForeignKey(BaseCourse, related_name='chapters', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
