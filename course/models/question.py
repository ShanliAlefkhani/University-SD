from django.db import models

from course.models.page import Page


class Question(Page):
    question_number = models.PositiveIntegerField()
    question_text = models.TextField()
