from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


class LoginPage(LoginView):
    template_name = 'account/login.html'
    success_url = "/"


def logged_out(request):
    logout(request,)
    return redirect("home")
