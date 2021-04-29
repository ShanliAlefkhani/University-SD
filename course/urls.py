from django.urls import path

from course.views import ChapterList, ChoiceList, CourseList, QuestionList

urlpatterns = [
    path('chapter-list/', ChapterList.as_view()),
    path('choice-list/', ChoiceList.as_view()),
    path('course-list/', CourseList.as_view()),
    path('question-list/', QuestionList.as_view()),
]
