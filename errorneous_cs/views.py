from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserCreate
from django.contrib.auth.decorators import login_required
from .decorders import unauthenticated_user
# Create your views here.


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You are Signed up, Plz Login!")
            return redirect('errorneous_cs:login')
    else:
        form = UserCreate()
    return render(request, 'errorneous_cs/register.html', {'form': form})


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('errorneous_cs:home')
    return render(request, 'errorneous_cs/login.html')


def logoutpage(request):
    logout(request)
    return redirect('errorneous_cs:login')


@login_required(login_url='errorneous_cs:login')
def home(request):
    return render(request, 'errorneous_cs/home.html')
