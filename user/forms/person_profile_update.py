from django import forms

from user.models import Person


class PersonProfileUpdateForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(),
        label='Name',
    )

    surname = forms.CharField(
        widget=forms.TextInput(),
        label='Surname',
    )

    birthday = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label='Birthday'
    )

    gender = forms.CharField(
        widget=forms.Select(choices=Person.GENDER_CHOICES),
        label='Gender'
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
        label='Email',
    )

    github_id = forms.CharField(
        widget=forms.TextInput(),
        label='Github ID',
    )

    linkedin_id = forms.CharField(
        widget=forms.TextInput(),
        label='LinkedIn ID',
    )
