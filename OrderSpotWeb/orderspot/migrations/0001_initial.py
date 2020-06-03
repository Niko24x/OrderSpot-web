# Generated by Django 3.0.3 on 2020-06-01 22:12

from django.db import migrations, models
import django.db.models.deletion
import orderspot.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=0, max_digits=7)),
                ('precio_individual', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('imagen', models.ImageField(upload_to=orderspot.models.imgProductos)),
                ('sku', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orderspot.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orderspot.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='EncabezadoPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('nit', models.CharField(blank=True, max_length=15, null=True)),
                ('nombre_factura', models.CharField(max_length=150)),
                ('direccion_factura', models.CharField(max_length=150)),
                ('direccion_entrega', models.CharField(max_length=150)),
                ('telefono_cliente', models.PositiveSmallIntegerField()),
                ('nombre_cliente', models.CharField(max_length=150)),
                ('codigo_de_entrada', models.CharField(max_length=150)),
                ('notas_adicionales', models.TextField()),
                ('estado', models.CharField(choices=[('Solicitado', 'Solicitado'), ('Aprobado', 'Aprobado'), ('Cancelado', 'Cancelado'), ('Anulado', 'Anulado'), ('Entregado', 'Entregado')], default='Activo', max_length=10)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orderspot.Municipio')),
            ],
        ),
    ]
