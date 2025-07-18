from django.db import models

from accounts.models import ProfileModel

# Create your models here.

class EducationModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="educations")

    #First Education
    first_education = models.CharField(max_length=50, blank=True)
    first_mark = models.CharField(max_length=50, blank=True)
    first_edu_date = models.DateField(null=True)

    #Second Education
    second_education = models.CharField(max_length=50, blank=True)
    second_mark = models.CharField(max_length=50, blank=True)
    second_edu_date = models.DateField(null=True)


    def __str__(self):
        return f"{self.profile.user.username} - Education"

class CertificateModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="certificates")

    #First Certificate
    first_certificate = models.CharField(max_length=50, blank=True)
    first_cert_startdate = models.DateField(null=True)
    first_cert_enddate = models.DateField(null=True)
    #Second Certificate
    second_certificate = models.CharField(max_length=50, blank=True)
    second_cert_startdate = models.DateField(null=True)
    second_cert_enddate = models.DateField(null=True)
    #Third Certificate
    third_certificate = models.CharField(max_length=50, blank=True)
    third_cert_startdate = models.DateField(null=True)
    third_cert_enddate = models.DateField(null=True)
    #Fourth Certificate
    fourth_certificate = models.CharField(max_length=50, blank=True)
    fourth_cert_startdate = models.DateField(null=True)
    fourth_cert_enddate = models.DateField(null=True)
    def __str__(self):
        return f"{self.profile.user.username} - Certificate"
    


class ExperienceModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="experiences")
    summary = models.CharField(max_length=100, blank=True)
    #First Experience
    first_experience = models.CharField(max_length=50, blank=True)
    first_description1 = models.CharField(max_length=100, blank=True)
    first_description2 = models.CharField(max_length=100, blank=True)
    first_exp_startdate = models.DateField(null=True)
    first_exp_enddate = models.DateField(null=True)

    #Second Experience
    second_experience = models.CharField(max_length=50, blank=True)
    second_description1 = models.CharField(max_length=100, blank=True)
    second_description2 = models.CharField(max_length=100, blank=True)
    second_exp_startdate = models.DateField(null=True)
    second_exp_enddate = models.DateField(null=True)
    def __str__(self):
        return f"{self.profile.user.username} - Experience"
    

class ProjectModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="projects")
    #First Project 
    first_project = models.CharField(max_length=50, blank=True)
    first_github = models.CharField(max_length=100, blank=True)
    first_description1 = models.CharField(max_length=100, blank=True)
    first_description2 = models.CharField(max_length=100, blank=True)
    first_techstack = models.CharField(max_length=100, blank=True)

    #Second Project 
    second_project = models.CharField(max_length=50, blank=True)
    second_github = models.CharField(max_length=100, blank=True)
    second_description1 = models.CharField(max_length=100, blank=True)
    second_description2 = models.CharField(max_length=100, blank=True)
    second_techstack = models.CharField(max_length=100, blank=True)

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
