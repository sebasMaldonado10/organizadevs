from rest_framework.permissions import BasePermission
from .models import MiembroProyecto, Proyecto


class EsMiembroDelProyecto(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if isinstance(obj, Proyecto):
            proyecto = obj
        else:
            proyecto = obj.proyecto

        return MiembroProyecto.objects.filter(
            usuario=request.user,
            proyecto=proyecto
        ).exists()
    