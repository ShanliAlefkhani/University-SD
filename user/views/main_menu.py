from django.views.generic import TemplateView

from user.models import Person, Company


class MainMenu(TemplateView):
    template_name = "main_menu/main_menu.html"

    def get(self, request, **kwargs):
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
