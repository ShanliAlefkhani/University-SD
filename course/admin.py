from django.contrib import admin

from course.models import Chapter, Choice, Course, Question

admin.site.register(Chapter)
admin.site.register(Choice)
admin.site.register(Course)
admin.site.register(Question)
