from django import forms

from .models import Project, ProjectModule, Todo


class ProjectForm(forms.ModelForm):

    class Meta():
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date', 'related_diagram')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['description'].label = ""
        self.fields['start_date'].label = ""
        self.fields['end_date'].label = ""
        self.fields['related_diagram'].label = ""

        self.fields['name'].widget.attrs.update({'placeholder': 'Project Name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Project Description', 'rows': '3'})
        self.fields['start_date'].widget.attrs.update({'placeholder': 'Start Date'})
        self.fields['end_date'].widget.attrs.update({'placeholder': 'Deadline'})
        # self.fields['related_diagram'].widget.attrs.update({'class': 'btn btn-default btn-file'})


class ProjectModuleForm(forms.ModelForm):

    class Meta():
        model = ProjectModule
        fields = ('name', 'description', 'start_date', 'end_date', 'related_diagram')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['description'].label = ""
        self.fields['start_date'].label = ""
        self.fields['end_date'].label = ""
        self.fields['related_diagram'].label = ""

        self.fields['name'].widget.attrs.update({'placeholder': 'Module Name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Module Description', 'rows': '3'})
        self.fields['start_date'].widget.attrs.update({'placeholder': 'Start Date'})
        self.fields['end_date'].widget.attrs.update({'placeholder': 'Deadline'})


class TodoForm(forms.ModelForm):

    class Meta():
        model = Todo
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ""
        self.fields['title'].widget.attrs.update({'class': 'form-control add-todo', 'placeholder': 'Add Todo'})
