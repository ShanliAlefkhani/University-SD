from django.db import models

from course.models.page import Page


class Course(Page):
    course_text = models.TextField()
    code_example = models.TextField()
