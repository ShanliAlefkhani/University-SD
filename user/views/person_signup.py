from django.shortcuts import render ,redirect
from user.models.person import Person
from user.forms.PersonSignupForm import PersonSignUpForm
from django.contrib.auth import login, get_user_model, authenticate
from django.contrib.auth.models import User


def PersonSignUp(request):
    if request.user.is_authenticated:
        return redirect('/')
    personsignup_form = PersonSignUpForm(request.POST or None)

    print(personsignup_form.is_valid())
    print(personsignup_form)
    if personsignup_form.is_valid():
        username = personsignup_form.cleaned_data.get('username')
        name = personsignup_form.cleaned_data.get('name')
        surname = personsignup_form.cleaned_data.get('surname')
        email = personsignup_form.cleaned_data.get('email')
        birthday = personsignup_form.cleaned_data.get('birthday')
        gender = personsignup_form.cleaned_data.get('gender')
        password = personsignup_form.cleaned_data.get('password')

        user = User.objects.create(
                username=username,
        )
        user.set_password(password)
        user.save()

        Person.objects.create(
            user=user, name=name, surname=surname, email=email, birthday=birthday, gender=gender,
        )
        
        
        return redirect('/login')

    context = {
        'personsignup_form': personsignup_form
    }
    return render(request, 'person_signup_page/person_signup.html', context)