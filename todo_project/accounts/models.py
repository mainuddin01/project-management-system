from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.urlresolvers import reverse

# Create your models here.
class UserProfileManager(UserManager):
    pass

class UserProfile(AbstractUser):
    designation = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_images', null=True, blank=True)

    objects = UserProfileManager()
