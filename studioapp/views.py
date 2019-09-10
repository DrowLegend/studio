from django.shortcuts import render, redirect
from .models import Mirror, Photofon

# Create your views here.


def home(request):
    return redirect(studio_home)


def studio_home(request):
    return render(request, 'studioapp/home.html')


def mirror(request):
    mirrors = Mirror.objects.all()
    return render(request, 'studioapp/mirror.html', {
        'mirrors': mirrors,
    })


def order(request):
    return render(request, 'studioapp/ordering.html', {})

