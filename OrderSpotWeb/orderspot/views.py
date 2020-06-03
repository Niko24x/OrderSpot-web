from django.shortcuts import render
from .serializers import EncabezadoSerializer
from .models import *

from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser
# Create your views here.

