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
        fields = ['first_experience', 'summary', 'first_description1', 'first_description2', 'first_exp_startdate','first_exp_enddate','second_experience','second_description1','second_description2','second_exp_startdate','second_exp_enddate']

class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = ['first_education', 'first_mark', 'first_edu_date','second_education','second_mark',
                  'second_edu_date',]

class CertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateModel
        fields = ['first_certificate', 'first_cert_startdate','first_cert_enddate','second_certificate','second_cert_startdate','second_cert_enddate','third_certificate','third_cert_startdate','third_cert_enddate','fourth_certificate','fourth_cert_startdate','fourth_cert_enddate',]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['first_project', 'first_github','first_description1','first_description2','first_techstack','second_project', 'second_github','second_description1','second_description2','second_techstack']

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = ['languages', 'framework','tools','linguistic']