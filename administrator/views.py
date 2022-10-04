from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from main.models import Complain, ComplainTrack


@login_required
def all_complains(request):
    complain = Complain.objects.all()
    status = ComplainTrack.objects.filter(complain__in=complain)
    context = {"complain": complain, 'status': status}
    return render(request, "administrator/all_complains.html", context)


@login_required
def verify(request):
    return render(request, "administrator/verify.html")
