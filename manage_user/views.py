from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from login.models import UserProfile
from django.contrib.auth.models import User


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def edit_user(request, user_id):
    user = UserProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user.user)
        if form.is_valid():
            user = form.save()
            return redirect('manage_user:home')
    else:
        form = RegistrationForm(instance=user.user, initial={'databases':user.databases.all()})
    return render(request, 'add_user.html', {'form': form, 'user': user, 'button_text': 'Edit', 'form_title': 'Edit User'})

def delete_user(request, user_id):
    users = UserProfile.objects.get(user_id=user_id)
    users.user.delete()
    return redirect('manage_user:home')

def logout_user(request):
    logout(request)
    return redirect('login')

def add_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('manage_user:home')
    else:
        form = RegistrationForm()
    return render(request, 'add_user.html', {'form': form, 'button_text': 'Add', 'form_title': 'Add User'})


