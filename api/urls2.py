#django
from django.urls import path

#own
from .views import *

#3rd

app_name = 'api'
urlpatterns = [
	#path('token-auth/', views.obtain_auth_token),
	path('pedidos/', PedidoList.as_view(), name='pedidos'),
	path('productos/', ProductoList.as_view(), name='productos'),
	path('pedido/<pk>/', PedidoEstadoUpdate.as_view(), name='pedido_update'),
	path('detallepedido/<pk>/', PedidoDetalle.as_view(), name='detallepedido')

]
