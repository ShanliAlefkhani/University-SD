from rest_framework import generics

from user.models import Person
from user.serializers.profile import ProfileSerializer, ProfileUpdateSerializer


class Profile(generics.ListAPIView):
    queryset = Person
    serializer_class = ProfileSerializer


class ProfileUpdate(generics.ListAPIView):
    queryset = Person
    serializer_class = ProfileUpdateSerializer
