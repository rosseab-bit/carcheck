from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('/flota', views.flota, name='flota'),
    path('/newcar', views.newcar, name='newcar'),
    # otras rutas de la aplicación...
]
