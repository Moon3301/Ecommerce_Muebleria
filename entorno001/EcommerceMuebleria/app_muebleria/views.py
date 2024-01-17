from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from operator import indexOf
from re import X
import this
from typing import List

from urllib import request
from django import views
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


totalPagar = 0

def inicio (request):

    listado = CarroCompras.objects.all()
    contexto = {'Carro' : listado}

    return render (request, 'index.html', contexto)

def listarProductos(request):
    global totalPagar

    listado = Producto.objects.all()
    listadoCarro = CarroCompras.objects.all()

    contexto = {'listado' : listado, 'listadoCarro': listadoCarro,'Total': totalPagar}
    return render (request, 'index.html', contexto)




def detalleProductos(request, id):
    global totalPagar

    producto = Producto.objects.get(sku = id)
    listado = CarroCompras.objects.all()

    contexto  = {'Producto' : producto, 'ListaCarro' : listado}

    return render(request, 'DetalleProducto.html', contexto)

# Valida si existe el sku en el carro de compras

def validarSiExiste(id):

    lista = CarroCompras.objects.all()

    for i in lista:
        if id in str(i.sku):
            return True

    return False

# Logica aumento y decremento productos

def AumentarCantidadProductos(request,id):
    global totalPagar

    carro = CarroCompras.objects.get(sku = id)
    carro.cantidad += 1
    carro.save()
    totalPagar += carro.precio
    

    return redirect(to = "ProcesoCompra")

def DisminuirCantidadProductos(request,id):
    global totalPagar

    carro = CarroCompras.objects.get(sku = id)
    if carro.cantidad > 1 :

        carro.cantidad -= 1
        
        carro.save()

       
        totalPagar -= carro.precio
        
    else:
        carro.cantidad = 0
        totalPagar -= carro.precio
        carro.delete()
        return redirect(to = "ProcesoCompra")
        
    return redirect(to = "ProcesoCompra")

def AumentarCantidadCarroFlotante(request,id):
    global totalPagar

    carro = CarroCompras.objects.get(sku = id)
    carro.cantidad += 1
    carro.save()
    totalPagar += carro.precio
    

    return redirect(to = "inicio")

def DisminuirCantidadCarroFlotante(request,id):
    global totalPagar

    carro = CarroCompras.objects.get(sku = id)
    if carro.cantidad > 1 :

        carro.cantidad -= 1
        
        carro.save()

        totalPagar -= carro.precio
        
    else:
        carro.cantidad = 0
        totalPagar -= carro.precio
        carro.delete()
        return redirect(to = "inicio")
        
    return redirect(to = "inicio")



def eliminarTotalPagar(request):
    totalPagar = 0

    return redirect(to = "ProcesoCompra")

def agregar(id):
    global totalPagar

    producto = Producto.objects.get(sku = id)

    validacion = validarSiExiste(id)

    if(validacion == True):

        carro = CarroCompras.objects.get(sku = id)
        carro.cantidad += 1
        
        carro.save()
        
        totalPagar += carro.precio
        
    else:
        carro = CarroCompras()
        carro.sku = producto.sku
        carro.nombre = producto.nombre
        carro.precio = producto.precio
        carro.img = producto.img
        carro.cantidad = 1
        
        carro.save()

        totalPagar += carro.precio



def agregarAlCarro(request,id):
    
    agregar(id)
        
    return redirect(to = "ProcesoCompra")

def agregarDirecto(request, id):

    agregar(id)
    contexto ['mensaje'] = {}
    return redirect(to = "inicio")
    return render(request, 'index.html',)


def ProcesoCompra(request):

    carro = Carro()

    listado = CarroCompras.objects.all()
    
    contexto = {'Carro' : listado, 'Total' : totalPagar, 'carrito' : carro}

    return render(request, 'ProcesoCompra.html', contexto)


def EliminarProductoLista(request, id):
    global totalPagar

    producto = CarroCompras.objects.get(sku = id)

    val = (producto.precio * producto.cantidad)
    totalPagar -= val 

    if(totalPagar < 0):
        totalPagar = 0
    
    producto.delete()
        
    return redirect(to = "ProcesoCompra")

def EliminarProductoCarroFlotante(request, id):
    global totalPagar

    producto = CarroCompras.objects.get(sku = id)

    val = (producto.precio * producto.cantidad)
    totalPagar -= val 

    if(totalPagar < 0):
        totalPagar = 0
    
    producto.delete()
        
    return redirect(to = "inicio")


    

def formularioCompra(request):


    etapa = 1
    listado = CarroCompras.objects.all()
    contexto = {'formularioCliente' : ClienteForm, 'Etapa':etapa, 'Carro':listado, 'Total':totalPagar}

    if request.method  == 'POST':
        
        cliente = ClienteForm(request.POST)
        
        cliente.save()
        contexto['mensaje'] = 'Datos Guardados'
        etapa = 2
        return render(request,'formularioCompraF2.html',contexto)

    return render (request, 'formularioCompra.html', contexto)



# CARRO COMPRAS VERSION 2

def validar(id):

    carrito = Carro.prod
    
    for i in carrito:

        if i.sku in id:
            return True

    return False


def agregarV2(request, id):

    producto = Producto.objects.get(sku = id)

    validacion = validar(id)

    if validacion:

        carrito = Carro()

        if carrito.cantidad < 0:
            carrito.cantidad = 0
        else:
            carrito.cantidad += 1

        if carrito.TotalPagar < 0:
            carrito.TotalPagar = 0
            
        else:
            carrito.TotalPagar += producto.precio
            
        carrito.save()
        
    else:

        carritoNuevo = Carro()
        carritoNuevo.prod.append(producto)
        carritoNuevo.TotalPagar += producto.precio
        carritoNuevo.cantidad = 1
        carritoNuevo.save()

    return redirect(to = "ProcesoCompra")
        

