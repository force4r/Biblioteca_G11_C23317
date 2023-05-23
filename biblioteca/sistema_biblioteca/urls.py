from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('catalogo/<int:año>/', views.catalogo, name="catalogo"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('biblioteca/<int:año>/',views.biblioteca, name='biblioteca'),
    path('biblioteca/',views.biblioteca, name='biblioteca'),
    path('contacto/', views.contacto, name="contacto"),

]