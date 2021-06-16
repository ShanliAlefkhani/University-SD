from django.db import models

from course.models import Chapter
from course.models.page import Page


class Question(Page):
    text = models.TextField()

    def next(self):
        if self.number == self.chapter.questions.count():
            if Chapter.objects.count() == self.chapter.id:
                return 'http://127.0.0.1:8000/course/course-list/'
            return 'http://127.0.0.1:8000/course/chapter-detail/{}'.format(self.chapter.id + 1)
        return 'http://127.0.0.1:8000/course/question-detail/{}'.format(Question.objects.get(
            chapter=self.chapter, number=self.number + 1).id)
