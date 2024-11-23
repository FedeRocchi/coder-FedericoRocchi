from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def saludar(request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Este es el tìtulo de mí App</h1>")

def saludar_con_parametro(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse (f"{nombre} {apellido}")

def index(request):
    context = {"año": 2024}
    return render(request, "core/index.html", context)