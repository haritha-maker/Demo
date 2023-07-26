from django.shortcuts import render

from . models import Place
from . models import Team


def home(request):
    obj=Place.objects.all()
    person=Team.objects.all()
    return render(request,"home.html",{'result':obj,'team':person})
