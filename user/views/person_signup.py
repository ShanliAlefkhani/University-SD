from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.forms.person_signup import PersonSignUpForm
from user.models.person import Person


def person_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    person_signup_form = PersonSignUpForm(request.POST or None)

    if person_signup_form.is_valid():
        username = person_signup_form.cleaned_data.get('username')
        name = person_signup_form.cleaned_data.get('name')
        surname = person_signup_form.cleaned_data.get('surname')
        email = person_signup_form.cleaned_data.get('email')
        birthday = person_signup_form.cleaned_data.get('birthday')
        gender = person_signup_form.cleaned_data.get('gender')
        password = person_signup_form.cleaned_data.get('password')

        user = User.objects.create(
                username=username,
        )
        user.set_password(password)
        user.save()

        Person.objects.create(
            user=user, name=name, surname=surname, email=email, birthday=birthday, gender=gender,
        )

        return redirect("http://127.0.0.1:8000/user/login/")

    context = {
        'person_signup_form': person_signup_form
    }
    return render(request, 'person_signup.html', context)
