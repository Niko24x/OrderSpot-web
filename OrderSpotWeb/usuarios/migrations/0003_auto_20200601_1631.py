# Generated by Django 3.0.3 on 2020-06-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200601_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalusuario',
            name='telefono',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
