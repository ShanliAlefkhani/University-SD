from django.views.generic import DetailView, UpdateView

from user.models import Company
from user.serializers.company_profile import CompanyProfileSerializer, CompanyProfileUpdateSerializer


class CompanyProfile(DetailView):
    queryset = Company.objects.all()
    serializer_class = CompanyProfileSerializer


class CompanyProfileUpdate(UpdateView):
    queryset = Company.objects.all()
    serializer_class = CompanyProfileUpdateSerializer
