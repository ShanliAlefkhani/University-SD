from django.urls import path, include

from user.views import person_signup, Profile, ProfileUpdate, login_user , company_signup

urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('person-signup/', person_signup),
    path('company-signup/', company_signup),
    path('profile/<pk>/', Profile.as_view()),
    path('profile-update/<pk>/', ProfileUpdate.as_view()),
    path('login/', login_user),
]
