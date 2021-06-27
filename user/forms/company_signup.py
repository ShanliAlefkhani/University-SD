from django import forms


class CompanySignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),
        label='Username',
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company\'s Name'}),
        label='Name',
    )

    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company\'s Address'}),
        label='Address',
    )

    creation_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label='Creation Date'
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Company\'s Email'}),
        label='Email',
    )

    website = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company\'s Website Address'}),
        label='Website',
    )

    telephone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company\'s Telephone Number'}),
        label='Telephone Number',
    )

    about = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter Company\'s Description & Goals'}),
        label='About',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        label='Password'
    )
