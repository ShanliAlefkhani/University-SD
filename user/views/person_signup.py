from django.contrib.auth.models import User
from rest_framework import generics
from django.views.generic.list import ListView
from user.serializers import PersonSerializer


class PersonSignUp(ListView):
    queryset = User.objects.all()
    serializer_class = PersonSerializer
    template_name = "person_signup_page/person_signup.html"
