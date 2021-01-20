from django.shortcuts import render, redirect
from .forms import formulariocontacto

# Create your views here.
def contacto(request):
    formulario_contacto = formulariocontacto()

    if request.method == "POST":
        formulario_contacto = formulariocontacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            telefono = request.POST.get("telefono")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            return redirect("/contacto/?valido")

    return render(request, "contacto/contacto.html", {'miformulario':formulario_contacto})
