from django.contrib import admin

from . models import ProfileModel
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProfileModel,ProfileAdmin)