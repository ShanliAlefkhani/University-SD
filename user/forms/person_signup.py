from django import forms

from user.models import Person


class PersonSignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Username'}),
        label='Username',
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
        label='Name',
    )

    surname = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Surname'}),
        label='Surname',
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),
        label='Email',
    )

    birthday = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label='Birthday'
    )

    gender = forms.CharField(
        widget=forms.Select(choices=Person.GENDER_CHOICES),
        label='Gender'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}),
        label='Password'
    )
