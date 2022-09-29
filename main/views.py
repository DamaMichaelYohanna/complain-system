import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main.forms import ComplainForm
from main.models import Complain, ComplainTrack


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
        ComplainTrack.objects.create(complain=complain)
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
    if request.method == "GET":
        filter_key = request.GET.get("search")
        if filter_key:
            if filter_key=="today":  # filter record for today only
                today = datetime.datetime.today().date()
                print(today)
                tracked_complain = ComplainTrack.objects.filter(complain__owner=request.user,
                                                            complain__date=today)
            elif filter_key=='seven days':  # filter record for the pass seven days
                last_seven_days = datetime.datetime.today() - datetime.timedelta(days=7)
                print(last_seven_days)
                tracked_complain = ComplainTrack.objects.filter(complain__owner=request.user,
                                                                complain__date__gt=last_seven_days.date())
            elif filter_key=='thirty days':  # filter record for the past 30 days.
                last_month = datetime.datetime.today() - datetime.timedelta(days=30)
                print(last_month)
                tracked_complain = ComplainTrack.objects.filter(complain__owner=request.user,
                                                                complain__date__gt=last_month.date())
            elif filter_key=='last three month':  # filter record for the past 90 days.
                last_three_month = datetime.datetime.today() - datetime.timedelta(days=30)
                tracked_complain = ComplainTrack.objects.filter(complain__owner=request.user,
                                                                complain__date__gt=last_three_month)
            else:
                tracked_complain = ComplainTrack.objects.filter(complain__owner=request.user)

        else:
            tracked_complain = ComplainTrack.objects.filter(complain__owner=request.user)

        context = {'complain': tracked_complain}
        return render(request, 'main/track_complain.html', context)