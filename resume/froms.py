from django import forms
from .models import ProfileModel
# forms.py
from django import forms
from .models import ProfileModel
from resume.models import ExperienceModel
class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['name', 'image', 'email', 'phone_number', 'github', 'linkedin']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = ['name', 'summary', 'description1', 'description2', 'date',]

