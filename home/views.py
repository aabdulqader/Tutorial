from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages






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
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account has been created succesfully')
            login(request, user)
            messages.info(request, f'{username}! Your are now login')
            return redirect('home:home')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')
    context = {
        'form':form, 
    }
    return render (request, 'register.html', context)
