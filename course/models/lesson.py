from django.db import models

from course.models.page import Page


class Lesson(Page):
    name = models.CharField(max_length=100)
    text = models.TextField()
    code_example = models.TextField()

    def next(self):
        if self.number == self.chapter.lessons.count():
            return 'http://127.0.0.1:8000/course/question-detail/{}'.format(self.chapter.questions.first().id)
        return 'http://127.0.0.1:8000/course/lesson-detail/{}'.format(Lesson.objects.get(
            chapter=self.chapter, number=self.number + 1).id)
