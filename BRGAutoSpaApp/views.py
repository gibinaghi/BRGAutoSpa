from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "BRGAutoSpaApp/home.html")

def servicios(request):
    return render(request, "BRGAutoSpaApp/servicios.html")

def tienda(request):
    return render(request, "BRGAutoSpaApp/tienda.html")

def bolg(request):
    return render(request, "BRGAutoSpaApp/blog.html")

def contacto(request):
    return render(request, "BRGAutoSpaApp/contacto.html")
