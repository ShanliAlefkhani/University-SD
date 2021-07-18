from django.db import models
from django.db.models import Sum

from course.models import BaseCourse


class Course(models.Model):
    base_course = models.ForeignKey(BaseCourse, related_name='course_status', on_delete=models.CASCADE)
    last_answered_question = models.PositiveIntegerField(default=1)

    @property
    def status(self):
        number_of_questions = 0
        for chapter in self.base_course.chapters.all():
            number_of_questions += chapter.questions.count()
        return self.last_answered_question / number_of_questions * 100
