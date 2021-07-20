from django.views.generic.detail import DetailView

from course.models import BaseCourse
from course.serializers import CourseSerializer
from user.models import Person


class CourseDetailView(DetailView):
    queryset = BaseCourse.objects.all()
    serializer_class = CourseSerializer
    template_name = "course_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data()
        course = BaseCourse.objects.get(id=self.kwargs['pk'])
        person = Person.objects.get(user=self.request.user)
        last_answered_question = person.get_first_course.last_answered_question
        number_of_questions = 0

        for chapter in course.chapters.all():
            number_of_questions += chapter.questions.count()
            if last_answered_question < number_of_questions:
                context['last_chapter'] = chapter.id
                return context
