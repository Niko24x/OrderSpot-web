# Generated by Django 3.0.3 on 2020-06-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderspot', '0002_auto_20200601_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encabezadopedido',
            name='telefono_cliente',
            field=models.PositiveIntegerField(),
        ),
    ]
