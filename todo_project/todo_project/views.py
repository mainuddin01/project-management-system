from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from projectmanager.models import Project, ProjectModule


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        total_projects = Project.objects.filter(user=self.request.user).count()
        running_projects = Project.objects.filter(user=self.request.user, working=True).count()
        completed_projects = Project.objects.filter(user=self.request.user, completed=True).count()
        context['total_projects'] = total_projects
        context['running_projects'] = running_projects
        context['completed_projects'] = completed_projects
        return context
