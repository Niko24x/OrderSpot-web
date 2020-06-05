#django
from django.urls import path

#own
from .views import *

#3rd
from rest_framework.authtoken import views

app_name="orderspot"
urlpatterns = [
	#path('api-token-auth/', views.obtain_auth_token),
]
