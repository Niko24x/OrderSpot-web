# Generated by Django 3.0.3 on 2020-06-25 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderspot', '0005_tipomedida'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='orderspot.TipoMedida'),
            preserve_default=False,
        ),
    ]
