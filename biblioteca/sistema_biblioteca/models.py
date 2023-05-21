from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=80, verbose_name="Apellido")
    class Meta:
        abstract =True
class Usuario(Persona):
    mail=models.EmailField(max_length=128, verbose_name="Email")
class Autor(Persona):
    nacionalidad = models.CharField(max_length=15, verbose_name="Nacionalidad", default="nacionalidad")
    
class Genero(models.Model):
    genero = models.CharField(max_length=20, verbose_name="Género", default="Género")

class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=0) #muchos a uno
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=0) #muchos a uno
    #models.CharField(max_length=200, verbose_name="Autor")
    isbn = models.BigIntegerField(verbose_name="ISBN") #son 13 digitos
    año_ingreso = models.IntegerField(verbose_name="Año de ingreso")
    año_edicion = models.IntegerField(verbose_name="Año de edición")
    descripcion = models.CharField(max_length= 3000, verbose_name="Descripcion", default="Descripcion")

class Editorial(models.Model):
    editorial = models.CharField(max_length=20, verbose_name="Editorial")
    libros=models.ManyToManyField(Libro)

class Idioma(models.Model):
    idioma = models.CharField(max_length=20, verbose_name="Idioma")
    libros=models.ManyToManyField(Libro)

