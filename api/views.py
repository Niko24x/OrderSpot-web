#django
from django.shortcuts import render
from django.http import JsonResponse

#own
from .serializers import *
from orderspot.models import *

#3rd
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser

# Create your views here.

################ API ##########################
#-------------- PEDIDOS -----------------#

class PedidoList(generics.ListAPIView):
	"""
		API devuelve pedidos en general
	"""
	queryset = EncabezadoPedido.objects.all()
	serializer_class = PedidoSerializer
	#permission_classes = []#definir

class PedidoFilter(filters.FilterSet):
	"""
		Filtro para pedidos
	"""
	nombre_factura = filters.CharFilter(lookup_expr='icontains')
	#fecha_solicitud = filters.CharFilter(lookup_expr='icontains') pendiente
	estado = filters.CharFilter(lookup_expr='icontains')
	nit = filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Producto
		fields = ['nombre_factura', 'estado', 'nit' ]

class PedidoListFiltered(generics.ListAPIView):

	"""
		API devuelve pedidos filtrado por usuario
	"""
	serializer_class = PedidoSerializer
	filterset_class = PedidoFilter

	def get_queryset(self):
		"""
		Retorna pedidos del usuario autenticado
		"""
		user = self.request.user
		return EncabezadoPedido.objects.filter(usuario=user)

class PedidoPartialUpdate(generics.UpdateAPIView):
	"""
		Utiliza patch para actualizar solo el estado
	"""
	queryset = EncabezadoPedido.objects.all()
	serializer_class = PedidoSerializer

	def patch(self, request, pk):
		model_object = EncabezadoPedido.objects.get(pk=pk)
		serializer = PedidoSerializer(model_object, data=request.data, partial=True) # set partial=True to update a data partially
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(data="wrong parameters", status=400)

#-------------- PRODUCTOS -----------------#
class ProductoFilter(filters.FilterSet):
	"""
		Filtro para productos
	"""
	nombre = filters.CharFilter(lookup_expr='icontains')
	categoria__nombre = filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Producto
		fields = ['nombre', 'categoria__nombre']

class ProductoList(generics.ListAPIView):
	"""
		API devuelve productos
	"""
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer
	#permission_classes = []#definir
	filterset_class = ProductoFilter

#-------------- PEDIDOS -----------------#

