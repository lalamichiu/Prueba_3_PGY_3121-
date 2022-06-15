from django.urls import path
from .views import home,Contacto,QuienesSomos,Donaciones,Tiendas

urlpatterns = [
    path('', home,name="home"),
    path('Contacto/', Contacto, name="contacto"),
    path('QuienesSomos/',QuienesSomos,name="Quienes somos"),
    path('Donaciones/',Donaciones,name="Donaciones"),
    path('Tiendas/',Tiendas,name="Tiendas")
]