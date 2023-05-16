from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    autor = models.CharField(max_length=200, verbose_name="Autor")
    isbn = models.BigIntegerField(verbose_name="ISBN")
    idioma = models.CharField(max_length=10, default= "Español", verbose_name="Idioma")
    año_ingreso = models.IntegerField(verbose_name="Año de ingreso")
    año_edicion = models.IntegerField(verbose_name="Año de edición")
   
    

class Autor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=80, verbose_name="Apellido")
    nacionalidad = models.CharField(max_length=15, verbose_name="Nacionalidad", default="nacionalidad")

class Genero(models.Model):
    genero = models.CharField(max_length=20, verbose_name="Género")

class Editorial(models.Model):
    editorial = models.CharField(max_length=20, verbose_name="Editorial")