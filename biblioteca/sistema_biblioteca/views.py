from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index (request):
   print(reverse('agregar_libro'))
   print(request.method)
   context={}
   
   return render(request,'sistema_biblioteca/index.html', context)

def catalogo(request):
   print(request.method)
   catalogo = [
      {
         'nombre_autor':'Jorge Luis',
         'apellido_autor':'Borges',
         'nombre_libro':'El Aleph',
         'año_edicion': 2015
      },
      {
         'nombre_autor':'Jorge Luis',
         'apellido_autor':'Borges',
         'nombre_libro':'El Inmortal',
         'año_edicion': 2006
      },

      {
         'nombre_autor':'Jorge Luis',
         'apellido_autor':'Borges',
         'nombre_libro':'El Sur',
         'año_edicion': 2020
      },
      {
         'nombre_autor':'Bram',
         'apellido_autor':'Stoker',
         'nombre_libro':'Drácula',
         'año_edicion': 2015
      },
      {
         'nombre_autor':'Alejandro',
         'apellido_autor':'Dumas',
         'nombre_libro':'El Conde de Montecristo',
         'año_edicion': 2010
      },
   ]    
   context = {
      'user_name': 'Carlos',
      'user_lastname': 'Lopez',
      'cat_lista': catalogo,
   }       

   return render(request,'sistema_biblioteca/catalogo.html', context)


def agregar_libro(request):
   return HttpResponse("Agregar libro")

def eliminar_libro(request):
   return HttpResponse("Eliminar libro")

def agregar_autor(request):
   return HttpResponse("Agregar autor")

def eliminar_autor(request):
   return HttpResponse("Eliminar autor")