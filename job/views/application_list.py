from django.views.generic import ListView

from job.models import Application
from job.serializers import ApplicationListSerializer


class ApplicationList(ListView):
    serializer_class = ApplicationListSerializer
    template_name = 'application_list.html'

    def get_queryset(self):
        return Application.objects.filter(job__company=self.request.user.company, job=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ApplicationList, self).get_context_data()
        context['pk'] = self.kwargs['pk']
        return context
