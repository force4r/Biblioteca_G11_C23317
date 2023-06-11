from django.db import models




class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=80, verbose_name="Apellido")
    class Meta:
        abstract =True
    
    def __str__(self):
        return f"{self.apellido} {self.nombre}"

class Lector(Persona):
    mail = models.EmailField(max_length=128, verbose_name="Email")
    dni = models.IntegerField(verbose_name="Dni", default=0000000)

class Bibliotecario(Persona):
    legajo = models.IntegerField(verbose_name="Legajo")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    dni = models.IntegerField(verbose_name="Dni", default=0000000)

class Autor(Persona):
    nacionalidad = models.CharField(max_length=15, verbose_name="Nacionalidad")
    
    def __str__(self):
        return super().__str__() + f" {self.nacionalidad}"


class Genero(models.Model):
    genero = models.CharField(max_length=20, verbose_name="Género", default="Género")

    def __str__(self):
        return f"{self.genero}"

class Editorial(models.Model):
    editorial = models.CharField(max_length=20, verbose_name="Editorial")

    def __str__(self):
        return f"{self.editorial}"

class Libro(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=0) #muchos a uno
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=0) #muchos a uno
    isbn = models.CharField(verbose_name="ISBN") #son 13 digitos
    año_ingreso = models.IntegerField(verbose_name="Año de ingreso")
    año_edicion = models.IntegerField(verbose_name="Año de edición")
    descripcion = models.TextField(max_length= 3000, verbose_name="Descripcion")
    editoriales = models.ManyToManyField(Editorial)
    idioma = models.CharField(verbose_name="Idioma", max_length=20)
    portada = models.ImageField(upload_to='images/', null=True, verbose_name="Portada")

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.isbn} - {self.año_ingreso} - {self.idioma} "
    
class Prestamo_Libro(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, verbose_name="Libro")
    fecha_prestamo_inicio = models.DateField(verbose_name="Inicio del prestamo")
    fecha_prestamo_fin = models.DateField(verbose_name="Fin del prestamo")
    lector = models.OneToOneField(Lector, on_delete=models.CASCADE, primary_key=True, verbose_name="Usuario asociado al préstamo")





