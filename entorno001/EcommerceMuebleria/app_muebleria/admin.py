from django.contrib import admin
from .models import Categoria, TipoProducto, Producto, Cliente, CarroCompras
# Register your models here.
admin.site.register(Categoria)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(CarroCompras)


