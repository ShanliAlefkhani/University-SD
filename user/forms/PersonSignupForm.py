from django import forms
from django.contrib.auth.models import User
from django.core import validators


Gender_Choices =(
    ('Female','Female'),
    ('Male','Male')
)

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
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email'}),
        label='Email',
    )

    birthday = forms.DateField(
        widget= forms.SelectDateWidget,
        label='Birthday'
    )

    gender = forms.CharField(
        widget=forms.Select(choices=Gender_Choices),
        label = 'Gender'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}),
        label='Password'
    )


    
