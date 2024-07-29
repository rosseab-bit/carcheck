from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    conductorname = models.CharField(max_length=100)
    dniconductor = models.IntegerField()
    modelovehiculo = models.CharField(max_length=100)
    patentevehiculo = models.CharField(max_length=100)
    modelovehiculo = models.CharField(max_length=100)
    capacidadvehiculo = models.CharField(max_length=100)
    estadovehiculo = models.CharField(max_length=100)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comentarios = models.CharField(max_length=100, null=True, blank=True)
