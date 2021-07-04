from django.urls import path

from course.views import CourseList, ChapterDetailView, CourseDetailView, LessonDetailView, QuestionDetailView

urlpatterns = [
    path('course-list/', CourseList.as_view()),
    path('chapter-detail/<int:pk>', ChapterDetailView.as_view()),
    path('course-detail/<int:pk>', CourseDetailView.as_view()),
    path('lesson-detail/<int:pk>', LessonDetailView.as_view()),
    path('question-detail/<int:pk>', QuestionDetailView.as_view()),
]
