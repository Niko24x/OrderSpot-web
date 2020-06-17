#django
from django.urls import path

#own
from .views import *

#3rd

app_name = 'api'
urlpatterns = [
	#pedidos
	path('pedidos/', PedidoList.as_view(), name='pedidos'),
	path('pedido_create/', PedidoCreate.as_view(), name='pedido_create'),
	path('pedido/<pk>/', PedidoEstadoUpdate.as_view(), name='pedido_estado_update'),
	path('pedidos_filtrados/', PedidoListFiltered.as_view(), name='pedidos_filtrados'),

	#detalle pedidos
	path('detallepedido/', PedidoDetalle.as_view(), name='detallepedido_cl'),
	path('detallepedido/<pk>/', PedidoDetalle2.as_view(), name='detallepedido'),

	#productos
	path('productos/', ProductoList.as_view(), name='productos'),

]
