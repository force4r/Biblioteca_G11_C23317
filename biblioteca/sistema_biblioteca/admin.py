from django.contrib import admin
from sistema_biblioteca.models import Libro, Editorial, Autor, Genero, Prestamo_Libro
# Register your models here.
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Prestamo_Libro)
