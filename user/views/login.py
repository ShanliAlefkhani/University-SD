from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from user.forms import LoginForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/user/main-menu/')
        else:
            login_form.add_error('username', 'A User With The Entered Profile Could Not Be Found')

    context = {
        'login_form': login_form
    }
    return render(request, 'login_page/login.html', context)
