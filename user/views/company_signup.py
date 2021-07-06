from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.forms import CompanySignUpForm
from user.models.company import Company


def company_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    company_signup_form = CompanySignUpForm(request.POST or None)

    if company_signup_form.is_valid():
        username = company_signup_form.cleaned_data.get('username')
        name = company_signup_form.cleaned_data.get('name')
        address = company_signup_form.cleaned_data.get('address')
        creation_date = company_signup_form.cleaned_data.get('creation_date')
        email = company_signup_form.cleaned_data.get('email')
        website = company_signup_form.cleaned_data.get('website')
        telephone_number = company_signup_form.cleaned_data.get('telephone_number')
        about = company_signup_form.cleaned_data.get('about')
        password = company_signup_form.cleaned_data.get('password')

        user = User.objects.create(
                username=username,
        )
        user.set_password(password)
        user.save()

        Company.objects.create(
            user=user, name=name, address=address, creation_date=creation_date, email=email, website=website, telephone_number=telephone_number, about=about,
        )

        return redirect("http://127.0.0.1:8000/user/login/")

    context = {
        'company_signup_form': company_signup_form
    }
    return render(request, 'company_signup.html', context)
