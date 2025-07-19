from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .utlis import user_directory
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from .utlis import user_directory


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    image = models.ImageField(null=True, upload_to=user_directory)
    email = models.EmailField(blank=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
