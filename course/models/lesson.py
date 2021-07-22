from django.db import models

from course.models import Chapter
from course.models.page import Page


class Lesson(Page):
    name = models.CharField(max_length=100)
    text = models.TextField()
    code_example = models.TextField()

    def next(self):
        try:
            if self.number == self.chapter.lessons.count():
                return 'http://127.0.0.1:8000/course/question-detail/{}'.format(self.chapter.questions.first().id)
        except:
            if Chapter.objects.count() == self.chapter.id:
                return 'http://127.0.0.1:8000/course/course-list/'
            return 'http://127.0.0.1:8000/course/chapter-detail/{}'.format(self.chapter.id + 1)

        return 'http://127.0.0.1:8000/course/lesson-detail/{}'.format(Lesson.objects.get(
            chapter=self.chapter, number=self.number + 1).id)
