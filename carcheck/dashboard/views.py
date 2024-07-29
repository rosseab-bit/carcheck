from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mapkick.django import Map
from .models import Vehiculo
import json

# Create your views here.
def dashboard(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    context = {
        'titulo': 'Ubicar',
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
    vehicles = Vehiculo.objects.all()
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    context = {
        'titulo': 'Bienvenido a Mi App',
        'contenido': 'Este es un ejemplo de cómo utilizar plantillas en Django.',
        'year': 2024,
        'map': map,
        'latitud': -34.60376,
        'longitud': -58.38162,
        'ruta_actual': request.path,
        'vehiculos': vehicles
    }
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/dashboard.html', context);


def newcar(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    context = {
        'titulo': 'Ubicar',
        'contenido': 'Este es un ejemplo de cómo utilizar plantillas en Django.',
        'year': 2024,
        'map': map,
        'latitud': -34.60376,
        'longitud': -58.38162,
        'ruta_actual': request.path
    }
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/dashboard.html', context);

def searchcar(request, patente_vehiculo):
    print('patente que se buscara: ', patente_vehiculo)
    vehicle = Vehiculo.objects.filter(patentevehiculo=patente_vehiculo)
    match_vehicles = {}
    if not vehicle:
        return JsonResponse({'vehicle':'Sin resultados'})
    else:
        for item in vehicle:
            if item.patentevehiculo == patente_vehiculo:
                match_vehicles['patente'] = patente_vehiculo
                match_vehicles['longitud'] = item.longitud
                match_vehicles['latitud'] = item.latitud
    return JsonResponse({'vehicle':match_vehicles}, status=200)

def loadnewcar(request):
    if request.method == 'POST':
        conductorname = request.POST.get('conductorname')
        dniconductor = request.POST.get('dniconductor')
        comentarios = request.POST.get('comentarios')
        modelovehiculo = request.POST.get('modelovehiculo')
        patentevehiculo = request.POST.get('patentevehiculo')
        modelovehiculo = request.POST.get('modelovehiculo')
        capacidadvehiculo = request.POST.get('capacidadvehiculo')
        estadovehiculo = request.POST.get('estadovehiculo')
        if not conductorname or not dniconductor or not comentarios or not modelovehiculo or not patentevehiculo or not modelovehiculo or not capacidadvehiculo or not estadovehiculo:
            return JsonResponse({'error': 'Todos los campos son obligatorios'})

        data = {
                'conductorname': conductorname,
                'dniconductor': dniconductor,
                'comentarios': comentarios,
                'modelovehiculo': modelovehiculo,
                'patentevehiculo': patentevehiculo,
                'modelovehiculo': modelovehiculo,
                'capacidadvehiculo': capacidadvehiculo,
                'estadovehiculo': estadovehiculo
                }
        vehicle = Vehiculo(**data)
        vehicle.save()
        vehicles = Vehiculo.objects.all()
        print('Data a guardar: ', data)
        for vehicle in vehicles:
            print('Dato guardado: ', vehicle.conductorname)
            print('Dato guardado: ', vehicle.dniconductor)
        return JsonResponse(data)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def updateposition(request):
    if request.method == 'POST':
        print('Body update geolocation: ')
        print(json.loads(request.body))
    return JsonResponse({'position': 'loaded'})
