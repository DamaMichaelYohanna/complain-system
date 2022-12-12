import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import ComplainForm
from main.models import Complain


def index(request):
    context = {}
    return render(request, 'main/index.html', context=context)


@login_required
def complain(request):
    if request.method == "POST":
        complain_form = ComplainForm(request.POST, request.FILES)
        print("passed")
        print(request.FILES)
        title = request.POST.get("title")
        body = request.POST.get("body")
        document = request.FILES.get("attachment")
        user = request.user
        complain = Complain.objects.create(title=title, body=body, attachment=document, owner=user)
        # ComplainTrack.objects.create(complain=complain)
        messages.success(request, "Your complain has been submitted. kindly check back later")
        return redirect("home")

    else:
        complain_form = ComplainForm()
    context = {"form": complain_form}
    return render(request, "main/complain.html", context)


def about(request):
    """about us page"""
    return render(request, "main/about.html")


def contact(request):
    """contact us page"""
    return render(request, 'main/contact.html')


@login_required
def track_complain(request):
   
    tracked_complain = Complain.objects.all()
    context = {'complain': tracked_complain}
    return render(request, 'main/tables.html', context)
