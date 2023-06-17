from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    dni = models.PositiveIntegerField(max_length=10, blank=True, null=True)
    legajo = models.CharField(max_length=10, blank=True)
