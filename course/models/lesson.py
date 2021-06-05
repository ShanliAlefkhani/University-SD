from django.db import models

from course.models.page import Page


class Lesson(Page):
    lesson_text = models.TextField()
    code_example = models.TextField()
