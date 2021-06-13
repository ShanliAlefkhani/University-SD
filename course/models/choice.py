from django.db import models

from course.models.question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.TextField()
    is_the_right_answer = models.BooleanField()
