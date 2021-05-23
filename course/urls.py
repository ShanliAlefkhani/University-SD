from django.urls import path

from course.views import ChapterList, ChoiceList, CourseList, QuestionList

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chapter-list/', ChapterList.as_view()),
    path('choice-list/', ChoiceList.as_view()),
    path('course-list/', CourseList.as_view()),
    path('question-list/', QuestionList.as_view()),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)