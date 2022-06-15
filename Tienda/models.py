from distutils.command.upload import upload
from pickle import TRUE
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField




class Marca(models.Model):
    id_marca=models.IntegerField(primary_key=True,verbose_name='ID Marca')
    nombre =models.CharField(max_length=50,blank=False,verbose_name='Nombre')
    def __str__(self):
        return(self.nombre)

class Producto(models.Model):
    id_producto=models.CharField(max_length=50,primary_key=True,verbose_name='ID Producto')
    nombre=models.CharField(max_length=50,blank=False,verbose_name='Nombre producto')
    descripcion=models.TextField(max_length=50,blank=False,verbose_name='Descripcion producto')
    precio=models.IntegerField(blank=False,verbose_name='Precio producto')
    nuevo=models.BooleanField(blank=False,verbose_name='Nuevo')
    marca=models.ForeignKey(Marca,on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField(blank=False,verbose_name='Fecha fabricacion')
    imagen=models.ImageField(upload_to="productos",null=True)
    def __str__(self):
        return(self.id_producto)