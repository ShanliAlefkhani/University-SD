from django.views.generic.detail import DetailView

from course.models import Question
from course.serializers import QuestionSerializer


class QuestionDetailView(DetailView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    template_name = 'question_detail_page/question_detail.html'
