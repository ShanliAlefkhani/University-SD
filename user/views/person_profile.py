from django.views.generic import UpdateView, TemplateView

from user.models import Person
from user.serializers.person_profile import PersonProfileUpdateSerializer


class PersonProfile(TemplateView):
    template_name = "person_profile.html"

    def get(self, request, **kwargs):
        kwargs['user'] = request.user
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = Person.objects.get(user=kwargs['user'])

        return context


class PersonProfileUpdate(UpdateView):
    queryset = Person.objects.all()
    serializer_class = PersonProfileUpdateSerializer
