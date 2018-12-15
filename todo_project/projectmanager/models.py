from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# Create your models here.
def proj_diagram_upload_to(instance, filename):
    username = instance.user.username
    project_name = instance.name
    project_slug = slugify(project_name)
    file_name, file_extension = filename.split(".")
    new_filename = "%s.%s" %(project_slug, file_extension)
    return "projects/%s/%s/%s" %(username, project_slug, new_filename)

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    working = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    related_diagram = models.ImageField(upload_to=proj_diagram_upload_to, null=True, blank=True)

    def set_importance_status(self):
        if self.important:
            self.important = False
        else:
            self.important = True
        self.save()
        return self.important

    def set_working_status(self):
        if self.working:
            self.working = False
        else:
            self.working = True
        self.save()
        return self.working

    def set_completion_status(self):
        if self.completed:
            self.completed = False
        else:
            self.completed = True
        self.save()
        return self.completed

    def set_activation_status(self):
        if self.active:
            self.active = False
        else:
            self.active = True
        self.save()
        return self.active

    def get_absolute_url(self):
        return reverse('projectmanager:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name



def module_diagram_upload_to(instance, filename):
    username = instance.project.user.username
    project_name = instance.project.name
    module_name = instance.name
    project_slug = slugify(project_name)
    module_slug = slugify(module_name)
    file_name, file_extension = filename.split(".")
    new_filename = "%s.%s" %(module_slug, file_extension)
    return "projects/%s/%s/module-%s-diagram/%s" %(username, project_slug, module_slug, new_filename)

class ProjectModule(models.Model):
    project = models.ForeignKey('Project')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    working = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    related_diagram = models.ImageField(upload_to=module_diagram_upload_to, null=True, blank=True)

    def set_importance_status(self):
        if self.important:
            self.important = False
        else:
            self.important = True
        self.save()
        return self.important

    def set_working_status(self):
        if self.working:
            self.working = False
        else:
            self.working = True
        self.save()
        return self.working

    def set_completion_status(self):
        if self.completed:
            self.completed = False
        else:
            self.completed = True
        self.save()
        return self.completed

    def set_activation_status(self):
        if self.active:
            self.active = False
        else:
            self.active = True
        self.save()
        return self.active

    def get_absolute_url(self):
        return reverse('projectmanager:modules', kwargs={'pk': self.project.pk, 'id': self.id})

    def __str__(self):
        return self.name




class Todo(models.Model):
    module = models.ForeignKey('ProjectModule')
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    important = models.BooleanField(default=False)
    working = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def set_importance_status(self):
        if self.important:
            self.important = False
        else:
            self.important = True
        self.save()
        return self.important

    def set_working_status(self):
        if self.working:
            self.working = False
        else:
            self.working = True
        self.save()
        return self.working

    def set_completion_status(self):
        if self.completed:
            self.completed = False
        else:
            self.completed = True
        self.save()
        return self.completed

    def set_activation_status(self):
        if self.active:
            self.active = False
        else:
            self.active = True
        self.save()
        return self.active

    def __str__(self):
        return self.title
