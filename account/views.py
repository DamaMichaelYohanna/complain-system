from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user.is_superuser:
            login(request, user)
            return redirect('/administrator')
        elif user:
            login(request, user)
            return redirect("/")
        else:
            print("wrong choice")
    else:
        template_name = 'account/login.html'
        return render(request, template_name, )


def logged_out(request):
    logout(request,)
    return redirect("home")
