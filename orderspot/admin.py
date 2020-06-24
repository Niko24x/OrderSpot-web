from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(EncabezadoPedido)
admin.site.register(DetallePedido)
admin.site.register(TipoMedida)