from django.contrib.auth.models import User
from rest_framework import generics

from user.serializers import PersonSerializer


class PersonSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PersonSerializer
