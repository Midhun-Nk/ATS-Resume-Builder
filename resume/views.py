from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resume.froms import ProfileForm, ExperienceForm,EducationForm,CertificateForm,SkillForm,ProjectForm
from resume.models import ExperienceModel

@login_required
def create_resume(request):
    user = request.user
    profile = user.profilemodel

    profile_form = ProfileForm(instance=profile)
    education_form = EducationForm()
    certificate_form = CertificateForm()
    skill_form = SkillForm()
    project_form = ProjectForm()
    experience_form = ExperienceForm()
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')

    context = {
        'profile_form': profile_form,
        'experience_form': experience_form,
        'education_form':education_form,
        'certificate_form':certificate_form,
        'skill_form':skill_form,
        'project_form':project_form
        
       
    }
    return render(request, 'views/createnew.html', context)
