from django.urls import path, include

from user.views import person_signup, PersonProfile, person_profile_update, login_user, company_signup, CompanyProfile, \
    CompanyProfileUpdate, MainMenu, logout_user

urlpatterns = [
    # path('', include('rest_framework.urls')),
    path('person-signup/', person_signup),
    path('company-signup/', company_signup),
    path('person-profile/', PersonProfile.as_view()),
    path('person-profile-update/', person_profile_update),
    path('company-profile/', CompanyProfile.as_view()),
    path('company-profile-update/', CompanyProfileUpdate.as_view()),
    path('login/', login_user),
    path('main-menu/', MainMenu.as_view()),
    path('logout/', logout_user)
]
