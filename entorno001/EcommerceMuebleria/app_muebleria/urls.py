from unicodedata import name
from django import contrib
from django import urls
from django.urls import path 
from django.contrib import admin
from django.urls.conf import include
from .views import *


urlpatterns = [

    path('',listarProductos ,name = "inicio"),
    path('detalleProductos/<id>',detalleProductos,name="detalleProductos"),
    path('ProcesoCompra/',ProcesoCompra, name ="ProcesoCompra"),
    path('formularioCompra/',formularioCompra,name="formularioCompra"),
    path('EliminarProductoLista/<id>',EliminarProductoLista,name="EliminarProductoLista"),
    path('EliminarProductoCarroFlotante/<id>',EliminarProductoCarroFlotante,name="EliminarProductoCarroFlotante"),
    path('agregarAlCarro/<id>',agregarAlCarro,name="agregarAlCarro"),
    path('AumentarCantidadProductos/<id>',AumentarCantidadProductos, name="AumentarCantidadProductos"),
    path('DisminuirCantidadProductos/<id>',DisminuirCantidadProductos,name="DisminuirCantidadProductos"),
    path('AumentarCantidadCarroFlotante/<id>',AumentarCantidadCarroFlotante,name="AumentarCantidadCarroFlotante"),
    path('DisminuirCantidadCarroFlotante/<id>',DisminuirCantidadCarroFlotante,name="DisminuirCantidadCarroFlotante"),
    path('eliminarTotalPagar',eliminarTotalPagar,name="eliminarTotalPagar"),
    path('agregarDirecto/<id>',agregarDirecto,name="agregarDirecto"),
    # Carrito version 2

    path('agregar/<id>',agregar,name="agregar")

]