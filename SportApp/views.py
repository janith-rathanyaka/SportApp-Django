from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.



def Home(request):
      
    context={
          "name":"JaNith RathNayaka",
          "number":12386656
    }

    return render(request, 'home.html',context)

def Sport(request):

    context={
     "list":{"cricket","football","vollyball"}
    }
    return render(request, 'sport.html',context)

def Contact(request):
    return render(request, 'contact.html')  