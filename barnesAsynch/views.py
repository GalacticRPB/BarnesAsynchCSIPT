from django.shortcuts import render
from django.http import HttpResponse


def mission(request):
    return render(request,"mission.html")

def vision(request):
    return render(request,"vision.html")

def objectives(request):
    return render(request,"objectives.html")