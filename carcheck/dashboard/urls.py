from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('/flota', views.flota, name='flota'),
    path('/newcar', views.newcar, name='newcar'),
    path('/loadnewcar', views.loadnewcar, name='loadnewcar'),
    path('/searchvehiculo/<str:patente_vehiculo>/', views.searchcar, name="searchcar"),
    path('/updateposition', views.updateposition, name='updateposition')
    # otras rutas de la aplicación...
]
