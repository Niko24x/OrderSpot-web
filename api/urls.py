#django
from django.urls import path

#own
from .views import *

#3rd

app_name = 'api'
urlpatterns = [
	#pedidos
	path('pedidos/', PedidoList.as_view(), name='pedidos'),
	path('pedidos/<pk>/', PedidoEstadoUpdate.as_view(), name='pedido_estado_update'),

	#detalle pedidos
	path('detallepedido/', PedidoDetalle.as_view(), name='detallepedido_cl'),
	path('detallepedido/<pk>/', PedidoDetalle2.as_view(), name='detallepedido'),

	#productos
	path('productos/', ProductoList.as_view(), name='productos'),

	#categorias
	path('categorias/', CategoriaList.as_view(), name='categorias'),

	#categorias
	path('departamentos/', DepartamentoList.as_view(), name='departamentos'),

	#categorias
	path('municipios/', MunicipioList.as_view(), name='municipios'),	

]
