from django.shortcuts import render
from .models import Tutorial

def home(request):
    context = {
        'tutorials':Tutorial.objects.all()
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")