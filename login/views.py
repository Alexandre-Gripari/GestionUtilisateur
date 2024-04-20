from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

def login(request):
    return LoginView.as_view(template_name='login.html')(request)