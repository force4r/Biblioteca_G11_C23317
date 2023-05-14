from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=200)
    isbn = models.IntegerField()
    idioma = models.CharField(max_length=10, default= "Español")
    año_ingreso = models.IntegerField()
    año_edicion = models.IntegerField()

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=80)