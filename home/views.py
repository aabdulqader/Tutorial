from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate





def home(request):
    context = {
        'tutorials':Tutorial.objects.all()
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            return redirect('home:home')
        else:
            for msg in form.error_messages:
                return(form.error_messages[msg])
    context = {
        'form':form, 
    }
    return render (request, 'register.html', context)
