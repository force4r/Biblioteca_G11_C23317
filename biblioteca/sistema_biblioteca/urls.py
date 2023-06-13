from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import include, path


urlpatterns = [
    path('', views.index, name="index"),
    path('catalogo/<int:año>/', views.catalogo, name="catalogo"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('biblioteca/<int:año>/',views.biblioteca, name='biblioteca'),
    path('biblioteca/',views.biblioteca, name='biblioteca'),
    path('alta_autor/', views.alta_autor, name="alta_autor"),
    path('alta_genero/', views.alta_genero, name="alta_genero"),
    path('alta_editorial/', views.alta_editorial, name="alta_editorial"),
    path('contacto/', views.contacto, name="contacto"),
]