#django
from django.db import models
from django.contrib.auth.models import AbstractUser

#3rd
from simple_history.models import HistoricalRecords

# Create your models here.

class Usuario(AbstractUser):
	administrador = 'Administrador'
	vendedor = 'Vendedor'
	TIPO_PERFIL = (
		(administrador, 'Administrador'),
		(vendedor, 'Vendedor'),
	)

	telefono = models.PositiveSmallIntegerField(default=1) 
	tipo_perfil = models.CharField(max_length=15, choices=TIPO_PERFIL, default = 'Vendedor')
	history = HistoricalRecords()

	def __str__(self):
		return self.username