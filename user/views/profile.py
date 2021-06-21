from django.views.generic import DetailView, UpdateView

from user.models import Person
from user.serializers.profile import ProfileSerializer, ProfileUpdateSerializer


class Profile(DetailView):
    queryset = Person.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdate(UpdateView):
    queryset = Person.objects.all()
    serializer_class = ProfileUpdateSerializer
