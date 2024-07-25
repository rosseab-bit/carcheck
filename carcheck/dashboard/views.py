from django.shortcuts import render
from django.http import HttpResponse
from mapkick.django import Map


# Create your views here.
def dashboard(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    context = {
        'titulo': 'Bienvenido a Mi App',
        'contenido': 'Este es un ejemplo de cómo utilizar plantillas en Django.',
        'year': 2024,
        'map': map,
        'latitud': -34.60376,
        'longitud': -58.38162,
        'ruta_actual': request.path
    }
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/dashboard.html', context);


def flota(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    context = {
        'titulo': 'Bienvenido a Mi App',
        'contenido': 'Este es un ejemplo de cómo utilizar plantillas en Django.',
        'year': 2024,
        'map': map,
        'latitud': -34.60376,
        'longitud': -58.38162,
        'ruta_actual': request.path
    }
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/dashboard.html', context);


def newcar(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    context = {
        'titulo': 'Bienvenido a Mi App',
        'contenido': 'Este es un ejemplo de cómo utilizar plantillas en Django.',
        'year': 2024,
        'map': map,
        'latitud': -34.60376,
        'longitud': -58.38162,
        'ruta_actual': request.path
    }
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/dashboard.html', context);
