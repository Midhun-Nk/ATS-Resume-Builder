from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .utlis import user_directory
# Create your models here.


class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField( max_length=50 , blank=True)
    image = models.ImageField(null=True,upload_to=user_directory)
    email = models.EmailField(blank=True)
    phone_number = models.IntegerField(blank=True)
    github = models.CharField( max_length=50 , blank=True)
    # linkedln = models.CharField( max_length=50 , blank=True)
    # education = models.OneToOneField(on_delete=models.CASCADE)
    # experince = models.OneToOneField(on_delete=models.CASCADE)
    # certificate = models.OneToOneField(on_delete=models.CASCADE)
    # project = models.OneToOneField(on_delete=models.CASCADE)
    # skills = models.OneToOneField(on_delete=models.CASCADE)