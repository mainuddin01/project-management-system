from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse

from .forms import ProjectForm, ProjectModuleForm, TodoForm

from .models import Project, ProjectModule, Todo

# Create your views here.
class ProjectView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        project_form = ProjectForm()

        user = self.request.user

        projects = Project.objects.filter(user=user)

        running_projects = Project.objects.filter(user=user, working=True)

        completed_projects = Project.objects.filter(user=user, completed=True)

        important_projects = Project.objects.filter(user=user, important=True)

        deactivated_projects = Project.objects.filter(user=user, active=False)

        if request.is_ajax():
            requested_id = request.GET.get('id')
            requested_state = request.GET.get('action')
            print(requested_id, requested_state)

            def perform_action(id, action):
                requested_project = get_object_or_404(Project, id=id)
                if action == "important":
                    current_status = requested_project.set_importance_status()
                elif action == "working":
                    current_status = requested_project.set_working_status()
                elif action == "completed":
                    current_status = requested_project.set_completion_status()
                if action == "deactivated":
                    current_status = requested_project.set_activation_status()
                return current_status

            current_status = perform_action(requested_id, requested_state)

            return JsonResponse({"current_status": current_status})



        context = {
            'projects': projects,
            'running_projects': running_projects,
            'completed_projects': completed_projects,
            'important_projects': important_projects,
            'deactivated_projects': deactivated_projects,
            'project_form': project_form,
        }
        return render(request, 'projectmanager/my_project.html', context)

    def post(self, request, *args, **kwargs):
        project_form = ProjectForm(request.POST)

        user = self.request.user

        projects = Project.objects.filter(user=user)

        running_projects = Project.objects.filter(user=user, working=True)

        completed_projects = Project.objects.filter(user=user, completed=True)

        important_projects = Project.objects.filter(user=user, important=True)

        deactivated_projects = Project.objects.filter(user=user, active=False)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = user
            project.save()

        context = {
            'projects': projects,
            'running_projects': running_projects,
            'completed_projects': completed_projects,
            'important_projects': important_projects,
            'deactivated_projects': deactivated_projects,
            'project_form': project_form,
        }
        return render(request, 'projectmanager/my_project.html', context)



class ModuleView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        module_form = ProjectModuleForm()

        user = self.request.user

        project_pk = self.kwargs.get('pk')

        project = get_object_or_404(Project, id=project_pk)

        modules = ProjectModule.objects.filter(project=project_pk)

        running_modules = ProjectModule.objects.filter(project=project_pk, working=True)

        completed_modules = ProjectModule.objects.filter(project=project_pk, completed=True)

        important_modules = ProjectModule.objects.filter(project=project_pk, important=True)

        deactivated_modules = ProjectModule.objects.filter(project=project_pk, active=False)

        if request.is_ajax():
            requested_id = request.GET.get('id')
            requested_state = request.GET.get('action')
            print(requested_id, requested_state)

            def perform_action(id, action):
                requested_module = get_object_or_404(ProjectModule, id=id)
                if action == "important":
                    current_status = requested_module.set_importance_status()
                elif action == "working":
                    current_status = requested_module.set_working_status()
                elif action == "completed":
                    current_status = requested_module.set_completion_status()
                if action == "deactivated":
                    current_status = requested_module.set_activation_status()
                return current_status

            current_status = perform_action(requested_id, requested_state)

            return JsonResponse({"current_status": current_status})

        context = {
            'project': project,
            'modules': modules,
            'running_modules': running_modules,
            'completed_modules': completed_modules,
            'important_modules': important_modules,
            'deactivated_modules': deactivated_modules,
            'module_form': module_form,
        }
        return render(request, 'projectmanager/project_modules.html', context)


    def post(self, request, *args, **kwargs):

        module_form = ProjectModuleForm(request.POST)

        project_pk = self.kwargs.get('pk')

        project = get_object_or_404(Project, id=project_pk)

        modules = ProjectModule.objects.filter(project=project_pk)

        running_modules = ProjectModule.objects.filter(project=project_pk, working=True)

        completed_modules = ProjectModule.objects.filter(project=project_pk, completed=True)

        important_modules = ProjectModule.objects.filter(project=project_pk, important=True)

        deactivated_modules = ProjectModule.objects.filter(project=project_pk, active=False)

        if module_form.is_valid():
            module = module_form.save(commit=False)
            module.project = project
            module.save()
            return HttpResponseRedirect(reverse_lazy('projectmanager:detail', kwargs={"pk": self.kwargs.get('pk')}))

        context = {
            'project': project,
            'modules': modules,
            'running_modules': running_modules,
            'completed_modules': completed_modules,
            'important_modules': important_modules,
            'deactivated_modules': deactivated_modules,
            'module_form': module_form,
        }
        return render(request, 'projectmanager/project_modules.html', context)



class TodoView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        if request.is_ajax():
            work_done = request.GET.get("completed")
            deactivate_work = request.GET.get('deactivate_id')
            if work_done:
                todo_obj = get_object_or_404(Todo, id=work_done)
                todo_obj.set_completion_status()

            if deactivate_work:
                todo_obj = get_object_or_404(Todo, id=deactivate_work)
                todo_obj.set_activation_status()

        todo_form = TodoForm()

        project_pk = self.kwargs.get('pk')

        module_id = self.kwargs.get('id')

        module = get_object_or_404(ProjectModule, id=module_id)

        available_todos = Todo.objects.filter(module=module_id, active=True, completed=False)
        completed_todos = Todo.objects.filter(module=module_id, active=True, completed=True)

        context = {
            'available_todos': available_todos,
            'completed_todos': completed_todos,
            'todo_form': todo_form,
            'project_pk': project_pk,
            'module': module,
            'module_id': module_id,
        }
        return render(request, 'projectmanager/todos.html', context)


    def post(self, request, *args, **kwargs):

        todo_form = TodoForm(request.POST)

        project_pk = self.kwargs.get('pk')

        module_id = self.kwargs.get('id')

        module = get_object_or_404(ProjectModule, id=module_id)

        available_todos = Todo.objects.filter(module=module_id, active=True, completed=False)
        completed_todos = Todo.objects.filter(module=module_id, active=True, completed=True)

        if todo_form.is_valid():
            todo = todo_form.save(commit=False)
            todo.module = module
            todo.save()
            return HttpResponseRedirect(reverse_lazy('home'))

        context = {
            'available_todos': available_todos,
            'completed_todos': completed_todos,
            'todo_form': todo_form,
            'project_pk': project_pk,
            'module': module,
            'module_id': module_id,
        }
        return render(request, 'projectmanager/todos.html', context)



class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projectmanager/project_list.html"


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm


class ModuleUpdateView(LoginRequiredMixin, UpdateView):
    model = ProjectModule
    form_class = ProjectModuleForm
    template_name = 'projectmanager/module_form.html'

    def get_object(self, *args, **kwargs):
        super(ModuleUpdateView, self).get_object(*args, **kwargs)
        # project_pk = self.kwargs.get('pk')
        module_id = self.kwargs.get('id')
        module_obj = get_object_or_404(ProjectModule, id=module_id)
        return module_obj
    # success_url = reverse_lazy('projectmanager:list')
