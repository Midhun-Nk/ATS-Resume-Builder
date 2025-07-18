from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resume.froms import ProfileForm, ExperienceForm, EducationForm, CertificateForm, SkillForm, ProjectForm

@login_required
def create_resume(request):
    user = request.user
    profile = user.profilemodel  # assuming OneToOneField from User to ProfileModel

    # Initialize forms with instance data for GET method
    profile_form = ProfileForm(instance=profile)

    education_instance = profile.educations.all()
    education_form = EducationForm(instance=education_instance.first())

    experience_instance = profile.experiences.all()
    experience_form = ExperienceForm(instance=experience_instance.first())

    certificate_instance = profile.certificates.all()
    certificate_form = CertificateForm(instance=certificate_instance.first())

    skill_instance = profile.skills.all()
    skill_form = SkillForm(instance=skill_instance.first())

    project_instance = profile.projects.all()
    project_form = ProjectForm(instance=project_instance.first())

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
        
        else:
            # Print form errors in the console for debugging
            print("Profile Form Errors:", profile_form.errors)
            print("Education Form Errors:", education_form.errors)
            print("Certificate Form Errors:", certificate_form.errors)
            print("Skill Form Errors:", skill_form.errors)
            print("Project Form Errors:", project_form.errors)
            print("Experience Form Errors:", experience_form.errors)

    context = {
        'profile_form': profile_form,
        'education_form': education_form,
        'certificate_form': certificate_form,
        'skill_form': skill_form,
        'project_form': project_form,
        'experience_form': experience_form,
        'experience_instance': experience_instance,
        'education_instance': education_instance,
        'project_instance': project_instance,
        'skill_instance': skill_instance,
        'certificate_instance': certificate_instance,
    }

    return render(request, 'views/createnew.html', context)
