from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from user.forms.person_profile_update import PersonProfileUpdateForm
from user.models import Person


class PersonProfile(TemplateView):
    template_name = "person_profile.html"

    def get(self, request, **kwargs):
        if request.user.is_anonymous:
            return redirect('http://127.0.0.1:8000/')

        kwargs['user'] = request.user
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person'] = Person.objects.get(user=kwargs['user'])

        return context


def person_profile_update(request):
    if request.user.is_anonymous:
        return redirect('http://127.0.0.1:8000/')

    initial_data = {
        'name': Person.objects.get(user=request.user).name,
        'surname': Person.objects.get(user=request.user).surname,
        'email': Person.objects.get(user=request.user).email,
        'birthday': Person.objects.get(user=request.user).birthday,
        'gender': Person.objects.get(user=request.user).gender,
        'github_id': Person.objects.get(user=request.user).github_id,
        'linkedin_id': Person.objects.get(user=request.user).linkedin_id
    }
    person_profile_update_form = PersonProfileUpdateForm(request.POST or None, initial=initial_data)

    if person_profile_update_form.is_valid():
        name = person_profile_update_form.cleaned_data.get('name')
        surname = person_profile_update_form.cleaned_data.get('surname')
        email = person_profile_update_form.cleaned_data.get('email')
        birthday = person_profile_update_form.cleaned_data.get('birthday')
        gender = person_profile_update_form.cleaned_data.get('gender')
        github_id = person_profile_update_form.cleaned_data.get('github_id')
        linkedin_id = person_profile_update_form.cleaned_data.get('linkedin_id')

        person = Person.objects.get(user=request.user)
        person.name = name
        person.surname = surname
        person.email = email
        person.birthday = birthday
        person.gender = gender
        person.github_id = github_id
        person.linkedin_id = linkedin_id
        person.save()

        return redirect("http://127.0.0.1:8000/user/person-profile/")

    context = {
        'person_profile_update_form': person_profile_update_form
    }
    return render(request, 'person_profile_update.html', context)
