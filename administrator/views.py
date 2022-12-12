from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime


from main.models import Complain


@login_required
def all_complains(request):
    complain = Complain.objects.all()
    print(complain[0].date)
    prev_complain = complain.count()
    latest = complain.filter(date=str(datetime.datetime.now().date())).count()
    context = {"complain": complain, 'latest':latest, 'count': prev_complain}
    return render(request, "index.html", context)

@login_required
def count_prev_compl(request):
    prev_complain = Complain.objects.count()
    print(prev_complain)
    return render(request, "index.html", prev_complain)


@login_required
def verify(request):
    return render(request, "administrator/verify.html")
@login_required
def login(request):
    return render(request, "login.html")

@login_required
def tables(request):
    tracked_complain = Complain.objects.all()
    context = {'complain': tracked_complain} 
    return render(request, 'tables.html', context)

