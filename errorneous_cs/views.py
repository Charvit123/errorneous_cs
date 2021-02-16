from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreate, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def SignView(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "You are Signed up, Plz Login!")
            return redirect('account:login')
        else:
            messages.error(request, "Plz SigneUp again!")
    else:
        form = UserCreate()
    return render(request, 'errorneous_cs/register.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request,'Successfully Logged In')
                return redirect('account:home')
    else:
        form = LoginForm()
    return render(request, 'errorneous_cs/login.html', {'form': form})


def home(request):
    return render(request, 'errorneous_cs/dashboard.html')
