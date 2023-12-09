from xml.etree.ElementTree import tostring
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        inputF = request.POST
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('home')
        
    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            user = authenticate(request, username=user, password=passw)

            if user:
                login(request,user)
                return redirect('home')
            
    else:
        form = LoginForm()

    return render(request,"login.html", {'form':form})

def log_out(request):
    logout(request)
    return redirect("home")

