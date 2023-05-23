from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect 
from .forms import contactoForm, AltaLibro
from django.contrib import messages
from .models import Libro

# Create your views here.

def index(request):
   context = {}

   return render(request, 'sistema_biblioteca/index.html', context)


def catalogo(request, año=0):
   if int(año) < 2015 and int(año) != 0:
      return HttpResponseNotFound("<h4>No hay datos previos al año 2015.</h4>")

   libro = Libro.objects.all().order_by("-id")
   # idioma = Idioma.objects.all().order_by("-id")
   # editorial = Editorial.objects.all().order_by("-id")
   # idioma = Idioma.objects.all()
   # editorial = Editorial.objects.all()
   context = {
      'libro': libro,
      'año_ingreso': año,
      # 'idioma': idioma,
      # 'editorial': editorial,
   }
   return render(request, 'sistema_biblioteca/catalogo.html', context)


def biblioteca(request, año = 2022):
   l = Libro.objects.all()
   

   if request.method == "POST":
      form = AltaLibro(request.POST)

      if form.is_valid():
            # Guarde la instancia nueva
            form.save()

            # redirija
            messages.add_message(request, messages.SUCCESS, 'Libro dado de alta con éxito', extra_tags="alert alert-success list-unstyled")
            return redirect("catalogo")
      else:
         messages.error(request, 'Por favor revise los campos a completar', extra_tags="alert alert-danger list-unstyled")

   else:
      form = AltaLibro()
   context = {
      'form': form,
      'libro': l
   }
   return render(request,'sistema_biblioteca/biblioteca.html', context)


def contacto(request):
   if request.method == "POST":
      contacto_form = contactoForm(request.POST)

      if contacto_form.is_valid():
         contacto_form.cleaned_data['nombre']
         contacto_form.cleaned_data['email']
         contacto_form.cleaned_data['asunto']
         contacto_form.cleaned_data['destino']
         contacto_form.cleaned_data['mensaje']

         messages.success(request, '¡Gracias por contactarnos! Te estaremos respondiendo a la brevedad', extra_tags="alert alert-success list-unstyled")
         return HttpResponseRedirect(request.path_info)
      else:
         messages.error(request, 'Por favor revise los campos a completar', extra_tags="alert alert-danger list-unstyled")

   else:
      contacto_form = contactoForm()

   context = {'form': contacto_form}

   return render(request, 'sistema_biblioteca/contacto.html', context)

# def biblioteca(request, año=2022):
#    if request.method == 'POST':
#       biblioteca_form = bibliotecaform(request.POST)
#       #EditorialForm = EditorialForm(request.POST)

#       if biblioteca_form.is_valid():
#          titulo = biblioteca_form.cleaned_data['titulo']
#          genero = biblioteca_form.cleaned_data['genero']
#          autor = biblioteca_form.cleaned_data['autor']  
#          isbn = biblioteca_form.cleaned_data['isbn']
#          año_edicion = biblioteca_form.cleaned_data['año_edicion']
#          descripcion = biblioteca_form.cleaned_data['descripcion']
#          editoriales = biblioteca_form.cleaned_data['editoriales']
#          idiomas = biblioteca_form.cleaned_data['idiomas']


#          biblioteca = Libro(
#             titulo = titulo,
#             genero = genero,
#             autor = autor,
#             isbn = isbn,    
#             año_edicion = año_edicion,
#             descripcion = descripcion,
#             idiomas = idiomas,
#             editoriales = editoriales
#          )

#          biblioteca.save()
#          print(biblioteca_form.is_valid())

#          messages.success(request, 'La informacion ha sido cargada', extra_tags="alert alert-success list-unstyled")
#          return HttpResponseRedirect(request.path_info)
#       else:
#          messages.error(request, 'Por favor revise los campos a completar', extra_tags="alert alert-danger list-unstyled")

#    else:
#       biblioteca_form = bibliotecaform()
#    context = {
#       'form' : biblioteca_form,
#       'cat_lista': catalogo,
#       'año_ingreso': año,
#    } 
#    #context = { 'form' : biblioteca_form}
#    return render(request, 'sistema_biblioteca/biblioteca.html', context)
