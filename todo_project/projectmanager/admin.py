from django.contrib import admin

from .models import Project, ProjectModule, Todo

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectModule)
admin.site.register(Todo)
