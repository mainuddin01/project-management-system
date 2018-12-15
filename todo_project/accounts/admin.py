from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile
from .forms import UserProfileCreationForm, UserProfileChangeForm

# Register your models here.
class UserProfileAdmin(UserAdmin):
    model = UserProfile
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm

admin.site.register(UserProfile, UserProfileAdmin)
