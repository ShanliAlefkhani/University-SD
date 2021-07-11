from django.shortcuts import redirect
from django.views.generic import TemplateView


class StartPage(TemplateView):
    template_name = 'start_page.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect('http://127.0.0.1:8000/user/main-menu/')
        return super(StartPage, self).get(request, *args, **kwargs)
