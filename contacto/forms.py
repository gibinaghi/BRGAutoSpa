from django import forms

class formulariocontacto(forms.Form):

    nombre=forms.CharField(label='Nombre', required=True)
    apellido=forms.CharField(label='Apellido', required=True)
    telefono=forms.CharField(label='Telefono', required=True)
    email=forms.CharField(label='Email', required=True)
    contenido=forms.CharField(label='Contenido', widget=forms.Textarea)