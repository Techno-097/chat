
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Home, Not, Image, Useful, All

def home(request):
    a = Home.objects.all()
    b = Not.objects.all()
    c = Image.objects.all()
    d = Useful.objects.all()
    e = All.objects.all()


    context = {
        "home": a,
        "not": b,
        "image": c,
        "useful": d,
        "all": e,


    }


    return render( request, 'index.html', context)