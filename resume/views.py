from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resume.froms import ProfileForm, ExperienceForm, EducationForm, CertificateForm, SkillForm, ProjectForm

@login_required
def create_resume(request):
    user = request.user
    profile = user.profilemodel  # assuming OneToOneField from User to ProfileModel

    # Initialize empty forms (GET method)

    profile_form = ProfileForm(instance=profile)
    education_instance = profile.educations.first()
    education_form = EducationForm(instance=education_instance)

    experience_instance = profile.experiences.first()
    experience_form = ExperienceForm(instance=experience_instance)

    certificate_instance = profile.certificates.first()
    certificate_form = CertificateForm(instance=certificate_instance)

    skill_instance = profile.skills.first()
    skill_form = SkillForm(instance=skill_instance)

    project_instance = profile.projects.first()
    project_form = ProjectForm(instance=project_instance)


    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        education_form = EducationForm(request.POST)
        certificate_form = CertificateForm(request.POST)
        skill_form = SkillForm(request.POST)
        project_form = ProjectForm(request.POST)
        experience_form = ExperienceForm(request.POST)

        if (profile_form.is_valid() and education_form.is_valid() and certificate_form.is_valid()
            and skill_form.is_valid() and project_form.is_valid() and experience_form.is_valid()):
            
            profile_form.save()

            education = education_form.save(commit=False)
            education.profile = profile
            education.save()

            certificate = certificate_form.save(commit=False)
            certificate.profile = profile
            certificate.save()

            skill = skill_form.save(commit=False)
            skill.profile = profile
            skill.save()

            project = project_form.save(commit=False)
            project.profile = profile
            project.save()

            experience = experience_form.save(commit=False)
            experience.profile = profile
            experience.save()

            return redirect('home')

    context = {
        'profile_form': profile_form,
        'education_form': education_form,
        'certificate_form': certificate_form,
        'skill_form': skill_form,
        'project_form': project_form,
        'experience_form': experience_form,
    }
    return render(request, 'views/createnew.html', context)
