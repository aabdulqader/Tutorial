from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserFrom





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
    form = NewUserFrom
    if request.method == "POST":
        form = NewUserFrom(request.POST)
        if form.is_valid():
            user =form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account has been created succesfully')
            login(request, user)
            messages.info(request, f'{username}! Your are now login')
            return redirect('home:login')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')
    context = {
        'form':form, 
    }
    return render (request, 'register.html', context)


def logout_view(request):
    logout(request)
    messages.info(request, "logged out succesfully")
    return redirect("home:home")



def login_view(request):
    form =  AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)


            if user is not None:
                login(request, user)
                messages.info(request, f'{username}! Your are now logged in')
                return redirect('home:home')

            else:
                messages.error(request, f'Invalid username or password')
        else:
            messages.error(request, f'Invalid username or password')
    context = {
        'form':form, 
    }
    return render (request, 'login.html', context)