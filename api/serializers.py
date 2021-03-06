#django
from django.core.files.base import ContentFile

#own
from orderspot.models import *

#3rd
from rest_framework import serializers
########################## Categoria ##########################
class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ['pk','nombre', 'slug', 'estado']

########################## Productos ##########################
class ProductoSerializer(serializers.ModelSerializer):
	#pendiente
	#imagen = Base64ImageField()
	categoria = CategoriaSerializer()
	tipo = serializers.StringRelatedField()

	class Meta:
		model = Producto
		fields = ['pk','nombre', 'descripcion', 'precio', 'tipo' ,'imagen', 'sku', 'categoria', 'estado']

##########################Detalle Pedidos##########################

class DetallePedidoSerializer(serializers.ModelSerializer):	
	pedido = serializers.PrimaryKeyRelatedField(queryset=EncabezadoPedido.objects.all(), required=False)	
	producto_detalle = ProductoSerializer(source='producto', read_only=True)
	producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

	class Meta:
		model = DetallePedido
		fields = ['pk', 'pedido', 'producto', 'producto_detalle', 'cantidad', 'precio_individual']

##########################Pedidos##########################
class PedidoSerializer(serializers.ModelSerializer):
	detalles = DetallePedidoSerializer(many=True, required=False, default=None)
	class Meta:
		model = EncabezadoPedido
		fields = ['pk', 'usuario', 'fecha_solicitud', 'fecha_entrega', 'municipio', 'municipio', 'nit', 'nombre_factura', 'direccion_factura', 'direccion_entrega', 'telefono_cliente', 'nombre_cliente', 'codigo_de_entrada', 'notas_adicionales', 'estado', 'detalles']

	def create(self, validated_data):
		detalles_data = validated_data.pop('detalles')
		pedido = EncabezadoPedido.objects.create(**validated_data)

		if detalles_data:
			for detalle_data in detalles_data:
				DetallePedido.objects.create(pedido=pedido, **detalle_data)
		return pedido

class DepartamentoSerializer(serializers.ModelSerializer):	

	class Meta:
		model = Departamento
		fields = ['pk', 'nombre', 'estado']

class MunicipioSerializer(serializers.ModelSerializer):	
	departamento = DepartamentoSerializer(many=False)

	class Meta:
		model = Municipio
		fields = ['pk', 'nombre', 'departamento', 'estado']