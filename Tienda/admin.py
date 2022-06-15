from django.contrib import admin

from Tienda.models import Marca, Producto
from .models import Marca,Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre","precio","marca","nuevo","imagen"]
    list_editable=["precio"]
    search_fields=["nombre"]
    list_filter=["marca","nuevo","nombre"]
    list_per_page=5
# Register your models here.
admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)
