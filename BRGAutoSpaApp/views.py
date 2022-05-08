from django.shortcuts import render, HttpResponse
from carro.carro import Carro

# Create your views here.

def home(request):

    carro=Carro(request)
    return render(request, "BRGAutoSpaApp/home.html")

def bolg(request):
    return render(request, "BRGAutoSpaApp/blog.html")


