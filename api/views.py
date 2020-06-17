#django
from django.shortcuts import render
from django.http import JsonResponse

#own
from .serializers import *
from orderspot.models import *

#3rd
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.

################ API ##########################
#-------------- PEDIDOS -----------------#

class PedidoFilter(filters.FilterSet):
	"""
		Filtro para pedidos
	"""
	nombre_factura = filters.CharFilter(lookup_expr='icontains')
	#fecha_solicitud = filters.CharFilter(lookup_expr='icontains') pendiente
	estado = filters.CharFilter(lookup_expr='icontains')
	nit = filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = EncabezadoPedido
		fields = ['nombre_factura', 'estado', 'nit' ]

	def get_queryset(self):
		"""
		Retorna pedidos del usuario autenticado
		"""
		user = self.request.user
		return EncabezadoPedido.objects.filter(usuario=user)

class PedidoList(generics.ListCreateAPIView):
	"""
		API devuelve pedidos en general
	"""
	queryset = EncabezadoPedido.objects.all()
	serializer_class = PedidoSerializer
	permission_classes = [IsAuthenticated]
	filterset_class = PedidoFilter
	authentication_classes = [TokenAuthentication, SessionAuthentication]

	def get_queryset(self):
		"""
		Retorna pedidos del usuario autenticado
		"""
		user = self.request.user
		return EncabezadoPedido.objects.filter(usuario=user)

class PedidoEstadoUpdate(generics.UpdateAPIView):
	"""
		Utiliza patch para actualizar solo el estado
	"""
	queryset = EncabezadoPedido.objects.all()
	serializer_class = PedidoSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication, SessionAuthentication]

	def patch(self, request, pk):
		model_object = EncabezadoPedido.objects.get(pk=pk)
		serializer = PedidoSerializer(model_object, data=request.data, partial=True) # set partial=True to update a data partially
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(data="wrong parameters", status=400)

class PedidoDetalle(generics.ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class PedidoDetalle2(generics.RetrieveUpdateDestroyAPIView):
	"""
		Retorna el detalle y actualiza o quita
	"""
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoSerializer


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
	permission_classes = [IsAuthenticated]
	filterset_class = ProductoFilter
	authentication_classes = [TokenAuthentication, SessionAuthentication]