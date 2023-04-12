from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index (request):
   print(reverse('agregar_libro'))
   print(request.method)
   context={}
   
   return render(request,'sistema_biblioteca/index.html', context)

def agregar_libro(request):
   return HttpResponse("Agregar libro")

def eliminar_libro(request):
   return HttpResponse("Eliminar libro")

def agregar_autor(request):
   return HttpResponse("Agregar autor")

def eliminar_autor(request):
   return HttpResponse("Eliminar autor")