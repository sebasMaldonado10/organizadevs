from django.contrib import admin
from .models import Proyecto, MiembroProyecto, CategoriaLink, LinkProyecto

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(MiembroProyecto)
admin.site.register(CategoriaLink)
admin.site.register(LinkProyecto)


