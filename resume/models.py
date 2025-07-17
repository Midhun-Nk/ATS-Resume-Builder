from django.db import models

from accounts.models import ProfileModel

# Create your models here.

class EducationModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="educations")
    name = models.CharField(max_length=50, blank=True)
    mark = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.profile.user.username} - Education"

class CertificateModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="certificates")
    name = models.CharField(max_length=50, blank=True)
    mark = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.profile.user.username} - Certificate"


class ExperienceModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="experiences")
    name = models.CharField(max_length=50, blank=True)
    summary = models.CharField(max_length=100, blank=True)
    description1 = models.CharField(max_length=100, blank=True)
    description2 = models.CharField(max_length=100, blank=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.profile.user.username} - Experience"

class ProjectModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="projects")
    heading = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=100, blank=True)
    description1 = models.CharField(max_length=100, blank=True)
    description2 = models.CharField(max_length=100, blank=True)
    techstack = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - Project"


class SkillModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="skills")
    languages = models.CharField(max_length=100, blank=True)
    framework = models.CharField(max_length=100, blank=True)
    tools = models.CharField(max_length=100, blank=True)
    soft_skill = models.CharField(max_length=100, blank=True)
    linguistic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - Skills"
