from django.contrib import admin
from .models import ExperienceModel,ProjectModel,SkillModel,CertificateModel,EducationModel
# Register your models here.

class ExperienceAdmin(admin.ModelAdmin):
    pass

class CertificateAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass


class EducationAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExperienceModel,ExperienceAdmin,)
admin.site.register(CertificateModel,CertificateAdmin,)
admin.site.register(EducationModel,EducationAdmin,)
admin.site.register(SkillModel,SkillAdmin,)
admin.site.register(ProjectModel,ProjectAdmin,)
