from django.db import models
from django.conf import settings
from usuarios.models import UsuarioPersonalizado

# Create your models here.

from django.db import models
from django.conf import settings


class Proyecto(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PE', 'Pendiente'
        EN_CURSO = 'EC', 'En Curso'
        FINALIZADA = 'FI', 'Finalizada'

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    materia = models.CharField(max_length=50)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='proyectos_creados'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.EN_CURSO
    )

    def __str__(self):
        return self.nombre


class MiembroProyecto(models.Model):
    class Roles(models.TextChoices):
        OWNER = 'OW', 'Owner'
        MIEMBRO = 'MB', 'Miembro'

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='membresias'
    )
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='miembros'
    )
    rol = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.MIEMBRO
    )
    fecha_union = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'proyecto')

    def __str__(self):
        return f"{self.usuario} - {self.proyecto} - {self.rol}"
    
class CategoriaLink(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Categoria: {self.nombre}"

class LinkProyecto(models.Model):
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete= models.PROTECT,
        related_name= 'links'
    )
    titulo = models.CharField(max_length=50)
    url = models.URLField()
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(
        CategoriaLink,
        on_delete= models.PROTECT,
        related_name= 'links'
    )
    agregado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='links_agregados'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Link {self.titulo}"
