from django.shortcuts import render
from .forms import formulariocontacto

# Create your views here.
def contacto(request):
    formulario_contacto=formulariocontacto()
    return render(request, "contacto/contacto.html", {'miformulario':formulario_contacto})
