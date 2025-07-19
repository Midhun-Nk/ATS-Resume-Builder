from django import forms
from accounts.models import ProfileModel

# forms.py
from django import forms
from .models import ExperienceModel,CertificateModel,ProjectModel,SkillModel,EducationModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'image', 'location','email', 'phone_number', 'github', 'linkedin']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ['first_exp_title', 'first_summary', 'first_exp_place','first_description1', 'first_description2', 'first_exp_startdate','first_exp_enddate','second_exp_title', 'second_summary', 'second_exp_place','second_description1','second_description2','second_exp_startdate','second_exp_enddate']
        widgets = {
            'first_summary': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'second_summary': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        fields = ['first_college', 'first_degree','first_mark', 'first_edu_startdate','first_edu_enddate','second_college',
                  'second_degree',
                  'second_mark',
                  'second_edu_startdate','second_edu_enddate',]

class CertificateForm(forms.ModelForm):
    class Meta:
        model = CertificateModel
        fields = ['first_certificate', 'first_cert_date','second_certificate','second_cert_date','third_certificate','third_cert_date','fourth_certificate','fourth_cert_date',]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['first_project', 'first_github','first_description1','first_description2','first_techstack','second_project', 'second_github','second_description1','second_description2','second_techstack']

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = ['languages', 'framework','tools','linguistic','soft_skill']