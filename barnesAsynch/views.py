from django.shortcuts import render
from django.http import HttpResponse


def mission(request):
    return render(request,"mission.html")

def vision(request):
    vision = "In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration."
    return render(request,"vision.html")

def objectives(request):
    objectives = "MSEUF shall produce graduates who have research-based knowledge, leadership and management skills, and professionalism."
    return render(request,"objectives.html")