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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

################ API ##########################


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'nombre': user.first_name+user.last_name

        })



#-------------- PEDIDOS -----------------#

class PedidoFilter(filters.FilterSet):
	"""
		Filtro para pedidos
	"""
	nombre_factura = filters.CharFilter(lookup_expr='icontains')
	fecha_solicitud = filters.CharFilter(lookup_expr='exact')
	estado = filters.CharFilter(lookup_expr='exact')
	nit = filters.CharFilter(lookup_expr='icontains')
	usuario__username = filters.CharFilter(lookup_expr='exact')
	pk = filters.CharFilter(lookup_expr='exact')



	class Meta:
		model = EncabezadoPedido
		fields = ['pk','nombre_factura', 'estado', 'nit', 'fecha_solicitud' , 'usuario__username']

	

class PedidoList(generics.ListCreateAPIView):
	"""
		API devuelve pedidos en general
	"""
	queryset = EncabezadoPedido.objects.all()
	serializer_class = PedidoSerializer
	permission_classes = [IsAuthenticated]
	filterset_class = PedidoFilter
	authentication_classes = [TokenAuthentication, SessionAuthentication]

class PedidoEstadoUpdate(generics.UpdateAPIView):
	"""
		Utiliza patch para actualizar solo el estado
	"""
	queryset = EncabezadoPedido.objects.all()
	serializer_class = PedidoSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication, SessionAuthentication]

class DetallePedidoFilter(filters.FilterSet):
	"""
		Filtro para pedidos
	"""
	pedido = filters.NumberFilter()

	class Meta:
		model = DetallePedido
		fields = ['pedido']

class PedidoDetalle(generics.ListCreateAPIView):
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoSerializer
	permission_classes = [IsAuthenticated]
	filterset_class = DetallePedidoFilter
	authentication_classes = [TokenAuthentication, SessionAuthentication]


class PedidoDetalle2(generics.RetrieveUpdateDestroyAPIView):
	"""
		Retorna el detalle y actualiza o quita
	"""
	queryset = DetallePedido.objects.all()
	serializer_class = DetallePedidoSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication, SessionAuthentication]


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

########################## Categoria ##########################
class CategoriaList(generics.ListAPIView):

	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication, SessionAuthentication]


########################## Departamentno ##########################
class DepartamentoList(generics.ListAPIView):

	queryset = Departamento.objects.all()
	serializer_class = DepartamentoSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication, SessionAuthentication]

########################## Municipio ##########################
class MunicipioList(generics.ListAPIView):

	queryset = Municipio.objects.all()
	serializer_class = MunicipioSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [TokenAuthentication, SessionAuthentication]