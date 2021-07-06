from django.views.generic import UpdateView, TemplateView

from user.models import Company
from user.serializers.company_profile import CompanyProfileUpdateSerializer


class CompanyProfile(TemplateView):
    template_name = "company_profile.html"

    def get(self, request, **kwargs):
        kwargs['user'] = request.user
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(user=kwargs['user'])

        return context


class CompanyProfileUpdate(UpdateView):
    queryset = Company.objects.all()
    serializer_class = CompanyProfileUpdateSerializer
