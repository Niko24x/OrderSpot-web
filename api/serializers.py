#django
from django.core.files.base import ContentFile

#own
from orderspot.models import *

#3rd
from rest_framework import serializers

#python
import base64

#encode base 64
class Base64ImageField(serializers.ImageField):
	print('test')

	def to_representation(self, value):
		return value

	def to_internal_value(self, data):
		print (data)
		encoded_string = data
		# with open(data, "rb") as image_file:
		# 	encoded_string = base64.b64encode(image_file.read())
		# 	print(encoded_string)
		# 	print('test')
		return encoded_string

class DetallePedidoSerializer(serializers.ModelSerializer):		
	producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

	class Meta:
		model = DetallePedido
		fields = ['pk', 'producto', 'cantidad','precio_individual']


class PedidoListSerializer(serializers.ModelSerializer):
	detalles = serializers.SerializerMethodField()

	class Meta:
		model = EncabezadoPedido
		fields = ['pk', 'usuario', 'fecha_solicitud', 'fecha_entrega', 'municipio', 'municipio', 'nit', 'nombre_factura', 'direccion_factura', 'direccion_entrega', 'telefono_cliente', 'nombre_cliente', 'codigo_de_entrada', 'notas_adicionales', 'estado', 'detalles']


	def create(self, validated_data):
		print (validated_data)
		pedido = EncabezadoPedido.objects.create(**validated_data)
		detalles_data = validated_data.pop('detalles')

		if detalles_data:
			for detalle_data in detalles_data:
				DetallePedido.objects.create(pedido=pedido, **detalle_data)
		return pedido

	def get_detalles(self, obj):
		"""obj es una instancia de pedido. Retorna una lista de diccionarios"""
		queryset = DetallePedido.objects.filter(pedido= obj)
		return [DetallePedidoSerializer(m).data for m in queryset]

class PedidoSerializer(serializers.ModelSerializer):
	detalles = DetallePedidoSerializer(many=True)
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

class ProductoSerializer(serializers.ModelSerializer):
	#pendiente
	#imagen = Base64ImageField()
	categoria = serializers.SerializerMethodField()

	class Meta:
		model = Producto
		fields = ['pk','nombre', 'descripcion', 'precio', 'imagen', 'sku', 'categoria', 'estado']

	def get_categoria(self, obj):
		"""obj es una instancia de categoria. Retorna una lista de diccionarios"""
		queryset = Categoria.objects.filter(pedido= obj)
		return [DetallePedidoSerializer(m).data for m in queryset]

