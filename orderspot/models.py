from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Categoria(models.Model):
	Activo = "Activo"
	Inactivo = "Inactivo"
	ESTADO_CHOICES = (
		(Activo, "Activo"),
		(Inactivo, "Inactivo"),
	)

	nombre = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)
	estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

	def __str__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Categoria, self).save(*args, **kwargs)


class TipoMedida(models.Model):
	Activo = "Activo"
	Inactivo = "Inactivo"
	ESTADO_CHOICES = (
		(Activo, "Activo"),
		(Inactivo, "Inactivo"),
	)
	tipo = models.CharField(max_length=150)
	estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

	def __str__(self):
		return self.tipo

def imgProductos(instance, filename):
		return 'imagenes/{0}/{1}/{2}'.format(str(instance.categoria), instance.nombre, filename)

class Producto(models.Model):
	Activo = "Activo"
	Inactivo = "Inactivo"
	ESTADO_CHOICES = (
		(Activo, "Activo"),
		(Inactivo, "Inactivo"),
	)

	nombre = models.CharField(max_length=150)
	descripcion = models.TextField()
	precio = models.DecimalField(max_digits=7, decimal_places=2)
	imagen = models.ImageField(upload_to=imgProductos)
	sku = models.CharField(max_length=30)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
	#tipo = models.ForeignKey(TipoMedida, on_delete=models.PROTECT)
	estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

	def __str__(self):
		return self.nombre

class Departamento(models.Model):
	Activo = "Activo"
	Inactivo = "Inactivo"
	ESTADO_CHOICES = (
		(Activo, "Activo"),
		(Inactivo, "Inactivo"),
	)

	nombre = models.CharField(max_length=150)
	estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
	
	def __str__(self):
		return self.nombre

class Municipio(models.Model):
	Activo = "Activo"
	Inactivo = "Inactivo"
	ESTADO_CHOICES = (
		(Activo, "Activo"),
		(Inactivo, "Inactivo"),
	)

	nombre = models.CharField(max_length=150)
	departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
	estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')
	
	def __str__(self):
		return self.nombre

class EncabezadoPedido(models.Model):
	Solicitado = "Solicitado"
	Aprobado = "Aprobado"
	Cancelado = "Cancelado"
	Anulado = "Anulado"
	Entregado = "Entregado"
	ESTADO_CHOICES = (
		(Solicitado, "Solicitado"),
		(Aprobado, "Aprobado"),
		(Cancelado, "Cancelado"),
		(Anulado, "Anulado"),
		(Entregado, "Entregado"),
	)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
	fecha_solicitud = models.DateField(auto_now_add=True)
	fecha_entrega = models.DateField(null=True, blank=True)
	municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
	nit = models.CharField(max_length=15, null=True, blank=True)
	nombre_factura = models.CharField(max_length=150)
	direccion_factura = models.CharField(max_length=150)
	direccion_entrega = models.CharField(max_length=150)
	telefono_cliente = models.PositiveIntegerField()
	nombre_cliente = models.CharField(max_length=150)
	codigo_de_entrada = models.CharField(max_length=150)
	notas_adicionales = models.TextField()
	estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo')

	def __str__(self):
		return (str(self.pk) + " - " + str(self.usuario) + " - " + self.nit + " - " + str(self.fecha_solicitud))

class DetallePedido(models.Model):
	pedido = models.ForeignKey(EncabezadoPedido, related_name='detalles', on_delete=models.PROTECT)
	producto = models.ForeignKey(Producto, related_name='productos', on_delete=models.PROTECT)
	cantidad = models.DecimalField(max_digits=7, decimal_places=0)
	precio_individual = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return (str(self.pk) + " - " + str(self.pedido.pk) +  " - " + str(self.producto))


