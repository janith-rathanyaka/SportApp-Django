from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.



def Home(request):
    return HttpResponse("<h1>This is our Home page</h1>");

def Sport(request):
    return HttpResponse("<h1>This is our latest sport news</h1>");

def Contact(request):
    return HttpResponse("<h1>This is Concat us</h1>");   