from django.http import HttpResponse
from django.shortcuts import render

def About(request):
   # return HttpResponse('About')
   return render(request, 'About.html')

def Homepage(request):
    #return HttpResponse('Home Page')
    return render(request, 'Home.html')