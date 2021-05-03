from django.db import models

from course.models.chapter import Chapter


class Page(models.Model):
    number = models.PositiveIntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    class Meta:
        abstract = True
