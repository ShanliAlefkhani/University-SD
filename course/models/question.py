from django.db import models

from course.models.page import Page


class Question(Page):
    text = models.TextField()
