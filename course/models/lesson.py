from django.db import models

from course.models.page import Page


class Lesson(Page):
    name = models.CharField(max_length=100)
    lesson_text = models.TextField()
    code_example = models.TextField()
