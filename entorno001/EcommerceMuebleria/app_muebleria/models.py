from operator import mod
from statistics import mode
from tkinter import image_names
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 20)

    def __str__(self):
        return self.nombre


class TipoProducto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length= 40)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    sku = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    medidas = models.CharField(max_length=20)
    marca = models.CharField(max_length=30)
    stock = models.IntegerField()
    img = models.CharField(max_length=100)
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipoProducto = models.ForeignKey(TipoProducto, on_delete= models.CASCADE)
    descripcion = models.CharField(max_length= 200)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100, null=True)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.rut)



class CarroCompras(models.Model):

    sku = models.IntegerField()
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    img = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    

    def __str__(self):
        return str(self.sku)

    def __int__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session["carrito"]
        if not carro:
            self.session["carrito"] = {}
            self.carro = self.session["carrito"]
        else:
            self.carro = carro


class Carro(models.Model):

    prod = []

    productos = models.CharField(max_length=50, choices=prod)
    TotalPagar = models.IntegerField()
    cantidad  = models.IntegerField()

    










