from django.urls import path

from course.views import ChapterList, ChoiceList, LessonList, QuestionList, CourseList, ChapterDetailView, \
    ChoiceDetailView

urlpatterns = [
    path('chapter-list/', ChapterList.as_view()),
    path('choice-list/', ChoiceList.as_view()),
    path('lesson-list/', LessonList.as_view()),
    path('question-list/', QuestionList.as_view()),
    path('course-list/', CourseList.as_view()),
    path('chapter-detail/<int:pk>', ChapterDetailView.as_view()),
    path('choice-detail/<int:pk>', ChoiceDetailView.as_view()),
]
