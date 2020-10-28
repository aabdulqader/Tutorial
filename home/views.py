from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('bismisslahir rahmanir harim')

def about(request):
    return HttpResponse('about: bismisslahir rahmanir harim')

def contact(request):
    return HttpResponse('contact: bismisslahir rahmanir harim')