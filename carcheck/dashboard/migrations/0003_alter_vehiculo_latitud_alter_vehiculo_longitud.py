# Generated by Django 5.0.7 on 2024-07-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_vehiculo_comentarios_alter_vehiculo_dniconductor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='latitud',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
