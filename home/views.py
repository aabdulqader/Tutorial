from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserFrom




def single_slug(request, single_slug):

    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("published")
            series_urls[m] = part_one.tutorial_slug

            context={
                "tutorial_series": matching_series, "part_ones": series_urls
            }

        return render(request, 'serieses.html',context)

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]

    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        tutorials_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)
        context={
            "tutorial ": this_tutorial,
            "sidebar": tutorials_from_series,
            "this_tut_idx": this_tutorial_id
        }
                      

        return render(request,'tutorial_details.html', context)    

def home(request):
    context = {
        'categories':TutorialCategory.objects.all()
    }
    return render(request, "categories.html", context)


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