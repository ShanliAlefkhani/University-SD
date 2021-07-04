from django.views.generic import DetailView, UpdateView

from user.models import Person
from user.serializers.person_profile import PersonProfileSerializer, PersonProfileUpdateSerializer


class PersonProfile(DetailView):
    queryset = Person.objects.all()
    serializer_class = PersonProfileSerializer


class PersonProfileUpdate(UpdateView):
    queryset = Person.objects.all()
    serializer_class = PersonProfileUpdateSerializer
