from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from main.models import Complain


@login_required
def all_complains(request):
    complain = Complain.objects.all()
    context = {"complain": complain,}
    return render(request, "administrator/all_complains.html", context)


@login_required
def verify(request):
    return render(request, "administrator/verify.html")
