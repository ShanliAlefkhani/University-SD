from django import forms

from user.models import Person


class CompanySignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Username'}),
        label='Username',
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),
        label='Name',
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Address'}),
        label='Address',
    )

    creation_date  = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label='Creation Date'
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Company Email'}),
        label='Email',
    )

    website = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Website Address'}),
        label='Website',
    )

    telephone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Telephone Number'}),
        label='Telephone Number',
    )

    about = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Company Description & Goals'}),
        label='About',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}),
        label='Password'
    )
