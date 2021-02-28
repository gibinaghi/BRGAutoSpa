from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "BRGAutoSpaApp/home.html")

def bolg(request):
    return render(request, "BRGAutoSpaApp/blog.html")


