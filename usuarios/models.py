from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UsuarioPersonalizado(AbstractUser):
    email = models.EmailField(unique=True) # No se pueden repetir emails
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Soy {self.email}"
    
