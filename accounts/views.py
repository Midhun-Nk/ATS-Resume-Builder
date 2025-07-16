from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .froms import UserRegistrationForm
import ATS_Builder
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            return render(request,'views/home.html')
        else:
            messages.error(request,f'Login Failed')

    return render(request,'views/login.html')

@login_required
def home_view(request):
    return render(request,'views/home.html')


def register_view(request):
    
    if request.method == 'POST':
        register_forms = UserRegistrationForm(request.POST)
        if register_forms.is_valid():
            user = register_forms.save()
            login(request,user)
            messages.success(request,'Your account has been created successfully!')
            return redirect('home')
        else:
            messages.success(request,'Please correct the errors below.!')
    else:
        register_forms = UserRegistrationForm()



    return render(request,'views/register.html',{'register_forms':register_forms})


def logout_view(request):
    logout(request)
    return redirect('login')
