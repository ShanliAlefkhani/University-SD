from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from user.forms.company_profile_update import CompanyProfileUpdateForm
from user.models import Company


class CompanyProfile(TemplateView):
    template_name = "company_profile.html"

    def get(self, request, **kwargs):
        if request.user.is_anonymous:
            return redirect('http://127.0.0.1:8000/')

        kwargs['user'] = request.user
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.get(user=kwargs['user'])

        return context


def company_profile_update(request):
    if request.user.is_anonymous:
        return redirect('http://127.0.0.1:8000/')

    initial_data = {
        'name': Company.objects.get(user=request.user).name,
        'address': Company.objects.get(user=request.user).address,
        'creation_date': Company.objects.get(user=request.user).creation_date,
        'about': Company.objects.get(user=request.user).about,
        'email': Company.objects.get(user=request.user).email,
        'website': Company.objects.get(user=request.user).website,
        'telephone_number': Company.objects.get(user=request.user).telephone_number
    }
    company_profile_update_form = CompanyProfileUpdateForm(request.POST or None, initial=initial_data)

    if company_profile_update_form.is_valid():
        name = company_profile_update_form.cleaned_data.get('name')
        address = company_profile_update_form.cleaned_data.get('address')
        creation_date = company_profile_update_form.cleaned_data.get('creation_date')
        about = company_profile_update_form.cleaned_data.get('about')
        email = company_profile_update_form.cleaned_data.get('email')
        website = company_profile_update_form.cleaned_data.get('website')
        telephone_number = company_profile_update_form.cleaned_data.get('telephone_number')

        company = Company.objects.get(user=request.user)
        company.name = name
        company.address = address
        company.creation_date = creation_date
        company.about = about
        company.email = email
        company.website = website
        company.telephone_number = telephone_number
        company.save()

        return redirect("http://127.0.0.1:8000/user/company-profile/")

    context = {
        'company_profile_update_form': company_profile_update_form
    }
    return render(request, 'company_profile_update.html', context)
