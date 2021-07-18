from django.contrib import admin

from course.models import Chapter, Choice, Lesson, Question, BaseCourse, Course

admin.site.register(BaseCourse)
admin.site.register(Chapter)
admin.site.register(Choice)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Course)
