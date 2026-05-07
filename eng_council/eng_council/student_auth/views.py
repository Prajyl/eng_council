# student_auth/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm

def register_view(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can log in now.')
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'student_auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'student_auth/login.html')

@login_required
def dashboard_view(request):
    return render(request, 'student_auth/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')
