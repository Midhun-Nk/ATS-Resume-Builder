from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ProfileModel
from resume.models import (
    EducationModel, ExperienceModel, CertificateModel,
    ProjectModel, SkillModel
)

@receiver(post_save, sender=User)
def create_user_profile_with_submodels(sender, instance, created, **kwargs):
    if created:
        profile = ProfileModel.objects.create(user=instance)

        # Just create and attach to profile via ForeignKey
        EducationModel.objects.create(profile=profile)
        ExperienceModel.objects.create(profile=profile)
        CertificateModel.objects.create(profile=profile)
        ProjectModel.objects.create(profile=profile)
        SkillModel.objects.create(profile=profile)
