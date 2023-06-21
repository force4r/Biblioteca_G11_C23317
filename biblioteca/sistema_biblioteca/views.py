from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from .forms import contactoForm, AltaLibro, AltaAutor, AltaGenero, AltaEditorial, Reservas
from django.contrib import messages
from .models import Libro, Autor, Genero, Editorial, Prestamo_Libro
from django.contrib.auth.decorators import login_required, permission_required
from usuarios.models import Usuario
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
   context = {}

   return render(request, 'sistema_biblioteca/index.html', context)


def catalogo(request, año=0):

   libro = Libro.objects.all().order_by("-id")
   context = {
      'libro': libro,
      'año_ingreso': año,
   }
   return render(request, 'sistema_biblioteca/catalogo.html', context)


@permission_required("sistema_biblioteca.add_prestamo_libro")
def reserva(request):

   libro = Libro.objects.all().order_by("-id")

   if request.method == "POST":
      form = Reservas(request.POST)
      if form.is_valid():
         nueva_reserva = Prestamo_Libro.objects.create(
                     #Guarda el usuario activo
                  lector = Usuario.objects.get(pk=request.user.id),
                  libro = form.cleaned_data["libro"],
                  reserva = form.cleaned_data["reserva"],
         )
         
         nueva_reserva.save()
         
         #form.save()
         messages.add_message(request, messages.SUCCESS, 'Libro reservado', extra_tags="alert alert-success list-unstyled")

      else:
         messages.error(request, 'Por favor intente de nuevo', extra_tags="alert alert-danger list-unstyled")   
         return redirect("reserva")
      
   else:
      form = Reservas()
   context = {
      'libro': libro,
      'form': form,
   }
   return render(request, 'sistema_biblioteca/reserva.html', context)


class LibrosPrestadosPorUsuario(LoginRequiredMixin, ListView):
   model = Prestamo_Libro
   template_name = 'sistema_biblioteca/mis_reservas.html'
   paginate_by = 10

   def get_queryset(self):
      return Prestamo_Libro.objects.filter(lector=self.request.user).filter(reserva=True).order_by('fecha_prestamo_fin')


#logeo para poder dar de alta libro
@login_required(login_url="/usuarios/login_user")
def biblioteca(request, año = 2022):
   l = Libro.objects.all()
   if request.method == "POST":
      form = AltaLibro(request.POST, request.FILES)

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


def login(request):
   context={}

   return render(request, 'sistema_biblioteca/login.html', context)

#logeo para poder dar de alta autor
@login_required(login_url="/usuarios/login_user")
def alta_autor(request):

   a = Autor.objects.all()

   if request.method == "POST":
      form = AltaAutor(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, 'Autor dado de alta con éxito', extra_tags="alert alert-success list-unstyled")

      else:
         messages.error(request, 'Por favor revise los campos a completar', extra_tags="alert alert-danger list-unstyled")   
         return redirect("alta_autor")
      
   else:
      form = AltaAutor()
   context = {
      'form': form,
      'autor' : a
      }
   return render(request, 'sistema_biblioteca/alta_autor.html', context)

@login_required(login_url="/usuarios/login_user")
def alta_genero(request):

   g = Genero.objects.all()

   if request.method == "POST":
      form = AltaGenero(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, 'Genero dado de alta con éxito', extra_tags="alert alert-success list-unstyled")

      else:
         messages.error(request, 'Por favor revise los campos a completar', extra_tags="alert alert-danger list-unstyled")   
         return redirect("alta_genero")
      
   else:
      form = AltaGenero()
   context = {
      'form': form,
      'genero' : g
      }
   return render(request, 'sistema_biblioteca/alta_genero.html', context)

@login_required(login_url="/usuarios/login_user")
def alta_editorial(request):

   e = Editorial.objects.all()

   if request.method == "POST":
      form = AltaEditorial(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, 'Editorial dado de alta con éxito', extra_tags="alert alert-success list-unstyled")

      else:
         messages.error(request, 'Por favor revise el campo a completar', extra_tags="alert alert-danger list-unstyled")   
         return redirect("alta_editorial")
      
   else:
      form = AltaEditorial()
   context = {
      'form': form,
      'editorial' : e
      }
   return render(request, 'sistema_biblioteca/alta_editorial.html', context)
