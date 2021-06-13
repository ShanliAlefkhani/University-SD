from django.db import models

from course.models.page import Page


class Question(Page):
    question_text = models.TextField()
