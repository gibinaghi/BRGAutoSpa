from django.urls import path
from BRGAutoSpaApp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('servicios', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.bolg, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]