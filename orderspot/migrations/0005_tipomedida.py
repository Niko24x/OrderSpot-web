# Generated by Django 3.0.3 on 2020-06-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderspot', '0004_auto_20200602_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=150)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
            ],
        ),
    ]
