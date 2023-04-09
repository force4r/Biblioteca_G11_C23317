from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index(request):
   return HttpResponse("Bienvenido a la biblioteca")

def agregar_libro(request):
   return HttpResponse("Agregar libro")

def eliminar_libro(request):
   return HttpResponse("Eliminar libro")

def agregar_autor(request):
   return HttpResponse("Agregar autor")

def eliminar_autor(request):
   return HttpResponse("Eliminar autor")