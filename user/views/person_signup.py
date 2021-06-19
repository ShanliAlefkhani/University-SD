from django.shortcuts import render ,redirect
from user.forms.PersonSignupForm import PersonSignUpForm
from django.contrib.auth import login, get_user_model, authenticate


def PersonSignUp(request):
    if request.user.is_authenticated:
        return redirect('/')
    personsignup_form = PersonSignUpForm(request.POST or None)

    if personsignup_form.is_valid():
        user_name = personsignup_form.cleaned_data.get('user_name')
        name = personsignup_form.cleaned_data.get('name')
        surname = personsignup_form.cleaned_data.get('surname')
        email = personsignup_form.cleaned_data.get('email')
        birthday = personsignup_form.cleaned_data.get('birthday')
        gender = personsignup_form.cleaned_data.get('gender')
        password = personsignup_form.cleaned_data.get('password')
        User.objects.create_user(
            username=user_name, name=name, surname=surname, email=email, birthday=birthday, gender=gender, password=password,
        )
        return redirect('/login')

    context = {
        'personsignup_form': personsignup_form
    }
    return render(request, 'person_signup_page/person_signup.html', context)