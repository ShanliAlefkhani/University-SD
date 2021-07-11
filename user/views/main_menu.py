from django.shortcuts import redirect
from django.views.generic import TemplateView

from user.models import Person, Company


class MainMenu(TemplateView):
    template_name = "person_main_menu.html"

    def get_template_names(self):
        try:
            Company.objects.get(user=self.request.user)
            return "company_main_menu.html"
        except Company.DoesNotExist:
            Person.objects.get(user=self.request.user)
            return "person_main_menu.html"

    def get(self, request, **kwargs):
        if request.user.is_anonymous:
            return redirect('http://127.0.0.1:8000/')

        kwargs['user'] = request.user
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['name'] = Company.objects.get(user=kwargs['user']).name
        except Company.DoesNotExist:
            context['name'] = Person.objects.get(user=kwargs['user']).name

        return context
