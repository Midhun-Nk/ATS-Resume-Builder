from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


from resume.froms import ProfileForm,ExperienceForm


# Create your views here.
@login_required
def create_resume(request):
    profile = request.user.profilemodel
    profile_form = ProfileForm(instance=profile)
    experience_Form = ExperienceForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change to your actual redirect target
    context={
        'profile_form':profile_form,
        'experience_Form':experience_Form
        
    }
    return render(request, 'views/createnew.html', context)
