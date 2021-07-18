from django import forms


class CompanyProfileUpdateForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(),
        label='Company Name',
    )

    address = forms.CharField(
        widget=forms.TextInput(),
        label='Address',
    )

    creation_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        label='Creation Date'
    )

    about = forms.CharField(
        widget=forms.Textarea(),
        label='About',
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
        label='Email',
    )

    website = forms.CharField(
        widget=forms.TextInput(),
        label='Website',
    )

    telephone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company\'s Telephone Number'}),
        label='Telephone Number',
    )
