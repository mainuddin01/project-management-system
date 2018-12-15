from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import UserProfile
from projectmanager.models import Project, ProjectModule

# Create your views here.
class SignUp(CreateView):
    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

class EditProfile(UpdateView):
    model = UserProfile
    form_class = UserProfileChangeForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, *args, **kwargs):
        current_user = self.request.user
        return current_user


class ProfileDetail(DetailView):
    model = UserProfile
    template_name = 'accounts/user_profile.html'

    def get_object(self, *args, **kwargs):
        current_user = self.request.user
        return current_user

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetail, self).get_context_data(*args, **kwargs)
        total_projects = Project.objects.filter(user=self.request.user).count()
        running_projects = Project.objects.filter(user=self.request.user, working=True).count()
        completed_projects = Project.objects.filter(user=self.request.user, completed=True).count()
        context['total_projects'] = total_projects
        context['running_projects'] = running_projects
        context['completed_projects'] = completed_projects
        return context
