from django.shortcuts import redirect
from django.views.generic import TemplateView


class StartPage(TemplateView):
    template_name = 'start_page.html'

    def get(self, request, *args, **kwargs):
        if request.user is not None:
            return redirect('http://127.0.0.1:8000/user/main-menu/')
