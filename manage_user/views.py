from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from login.models import UserProfile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, choice=request.POST['choice'])
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def edit_user(request, user_id):
    user = UserProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user.user)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile.objects.get(user=user)
            user_profile.choice = request.POST['choice']
            user_profile.save()
            return redirect('manage_user:home')
    else:
        form = RegistrationForm(instance=user.user)
    return render(request, 'add_user.html', {'form': form, 'user': user, 'button_text': 'Edit'})

def delete_user(request, user_id):
    users = UserProfile.objects.get(user_id=user_id)
    users.user.delete()
    return redirect('manage_user:home')

def logout_user(request):
    return redirect('login')

def add_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, choice=request.POST['choice'])
            return redirect('manage_user:home')
    else:
        form = RegistrationForm()
    return render(request, 'add_user.html', {'form': form, 'button_text': 'Add'})


