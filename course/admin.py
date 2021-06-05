from django.contrib import admin

from course.models import Chapter, Choice, Lesson, Question, Course

admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Choice)
admin.site.register(Lesson)
admin.site.register(Question)
