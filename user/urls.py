from django.urls import path, include

from user.views import PersonSignUp, Profile, ProfileUpdate

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('person-signup/', PersonSignUp.as_view()),
    path('profile/<pk>/', Profile.as_view()),
    path('profile-update/<pk>/', ProfileUpdate.as_view()),
]
