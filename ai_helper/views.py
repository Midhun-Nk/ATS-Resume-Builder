from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile

@login_required
def generate_pdf(request):
    user = request.user
    profile = user.profilemodel

    context = {
        'profile': profile,
        'experiences': profile.experiences.all(),
        'educations': profile.educations.all(),
        'certificates': profile.certificates.all(),
        'projects': profile.projects.all(),
        'skills': profile.skills.all(),  
    }

    html_string = render_to_string('views/resume_pdf.html', context)

    # Optional: Save to a temp file
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Create response
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=resume.pdf'
    return response
