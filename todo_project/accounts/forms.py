from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta(UserCreationForm):
        model = UserProfile
        fields = ('username', 'email', 'designation', 'password1', 'password2', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Confirm Password'


class UserProfileChangeForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    designation = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta():
        model = UserProfile
        fields = ('first_name', 'last_name', 'designation', 'password', 'photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['photo'].label = 'Password'
