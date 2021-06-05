from django.db import models

from course.models.chapter import Chapter


class Page(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    class Meta:
        abstract = True
