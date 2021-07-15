from django.shortcuts import redirect
from django.views.generic.detail import DetailView

from course.models import Question
from course.serializers import QuestionSerializer
from user.models import Person


class QuestionDetailView(DetailView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    template_name = 'question_detail.html'

    def get(self, request, *args, **kwargs):
        course = Person.objects.get(user=request.user).courses.first()
        # if course.last_answered_question < kwargs["pk"]:
        #     return redirect('http://127.0.0.1:8000/course/question-detail/{}'.format(course.last_answered_question))
        course.last_answered_question = kwargs["pk"]
        course.save()
        return super(QuestionDetailView, self).get(request, args, kwargs)
