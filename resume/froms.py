from django import forms
from accounts.models import ProfileModel
# forms.py
from django import forms
from .models import ExperienceModel,CertificateModel,ProjectModel,SkillModel,EducationModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'image', 'email', 'phone_number', 'github', 'linkedin']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ['experience', 'summary', 'description1', 'description2', 'startdate','enddate',]

class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = ['education', 'mark', 'startdate','enddate',]

class CertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateModel
        fields = ['certificate', 'startdate','enddate',]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['project', 'github','description1','description2','techstack']

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = ['languages', 'framework','tools','linguistic']