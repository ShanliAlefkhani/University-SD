from django.urls import path, include

from user.views import person_signup, Profile, ProfileUpdate, login_user

urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('person-signup/', person_signup),
    path('profile/<pk>/', Profile.as_view()),
    path('profile-update/<pk>/', ProfileUpdate.as_view()),
    path('login/', login_user),
]
