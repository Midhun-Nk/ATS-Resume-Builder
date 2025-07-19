from django.db import models

from accounts.models import ProfileModel

# Create your models here.

class EducationModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="educations")

    #First Education
    first_college = models.CharField(max_length=200, blank=True)
    first_degree = models.CharField(max_length=200, blank=True)
    first_mark = models.CharField(max_length=200, blank=True)
    first_edu_startdate = models.DateField(null=True)
    first_edu_enddate = models.DateField(null=True)

    #Second Education
    second_college = models.CharField(max_length=200, blank=True)
    second_degree = models.CharField(max_length=200, blank=True)
    second_mark = models.CharField(max_length=200, blank=True)
    second_edu_startdate = models.DateField(null=True)
    second_edu_enddate = models.DateField(null=True)


    def __str__(self):
        return f"{self.profile.user.username} - Education"

class CertificateModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="certificates")

    #First Certificate
    first_certificate = models.CharField(max_length=200, blank=True)
    first_cert_date = models.DateField(null=True)
    #Second Certificate
    second_certificate = models.CharField(max_length=200, blank=True)
    second_cert_date = models.DateField(null=True)

    #Third Certificate
    third_certificate = models.CharField(max_length=200, blank=True)
    third_cert_date = models.DateField(null=True)
   
    #Fourth Certificate
    fourth_certificate = models.CharField(max_length=200, blank=True)
    fourth_cert_date = models.DateField(null=True)
    def __str__(self):
        return f"{self.profile.user.username} - Certificate"
    


class ExperienceModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="experiences")
    
    #First Experience
    first_summary = models.TextField(max_length=200, blank=True)
    first_exp_title = models.CharField(max_length=200, blank=True)
    first_exp_place = models.CharField(max_length=200, blank=True)
    first_description1 = models.CharField(max_length=200, blank=True)
    first_description2 = models.CharField(max_length=200, blank=True)
    first_exp_startdate = models.DateField(null=True)
    first_exp_enddate = models.DateField(null=True)

    #Second Experience
    second_summary = models.CharField(max_length=200, blank=True)
    second_exp_title = models.CharField(max_length=200, blank=True)
    second_exp_place = models.CharField(max_length=200, blank=True)
    second_description1 = models.CharField(max_length=200, blank=True)
    second_description2 = models.CharField(max_length=200, blank=True)
    second_exp_startdate = models.DateField(null=True)
    second_exp_enddate = models.DateField(null=True)
    def __str__(self):
        return f"{self.profile.user.username} - Experience"
    

class ProjectModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="projects")
    #First Project 
    first_project = models.CharField(max_length=200, blank=True)
    first_github = models.CharField(max_length=200, blank=True)
    first_description1 = models.CharField(max_length=200, blank=True)
    first_description2 = models.CharField(max_length=200, blank=True)
    first_techstack = models.CharField(max_length=200, blank=True)

    #Second Project 
    second_project = models.CharField(max_length=200, blank=True)
    second_github = models.CharField(max_length=200, blank=True)
    second_description1 = models.CharField(max_length=200, blank=True)
    second_description2 = models.CharField(max_length=200, blank=True)
    second_techstack = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - Project"


class SkillModel(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="skills")
    languages = models.CharField(max_length=200, blank=True)
    framework = models.CharField(max_length=200, blank=True)
    tools = models.CharField(max_length=200, blank=True)
    soft_skill = models.CharField(max_length=200, blank=True)
    linguistic = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.profile.user.username} - Skills"
