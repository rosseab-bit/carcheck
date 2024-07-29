from django.contrib import admin
from .models import Vehiculo

# Register your models here.
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('conductorname', 'dniconductor', 'modelovehiculo', 'patentevehiculo', 'modelovehiculo', 'capacidadvehiculo', 'estadovehiculo', 'longitud', 'longitud', 'timestamp', 'comentarios')
