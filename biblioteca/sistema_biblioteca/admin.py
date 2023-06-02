from django.contrib import admin
from sistema_biblioteca.models import Libro, Editorial, Autor, Genero, Lector, Bibliotecario
# Register your models here.
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Lector)
admin.site.register(Bibliotecario)
