from django.shortcuts import render
from .models import Producto

# Create your views here.
def home (request):
    return render(request,'Tienda/home.html')

def Contacto (request):
    return render(request,'Tienda/Contacto.html')

def Donaciones (request):
    return render(request,'Tienda/Donaciones.html')

def QuienesSomos (request):
    return render(request,'Tienda/QuienesSomos.html')

def Tiendas (request):
    productos = Producto.objects.all()
    data = {'productos':productos}

    return render(request,'Tienda/Tiendas.html',data)




