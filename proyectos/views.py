from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import CategoriaLink, LinkProyecto, MiembroProyecto, Proyecto
from .serializers import (
    CategoriaLinkSerializer,
    LinkProyectoSerializer,
    MiembroProyectoSerializer,
    ProyectoSerializer
)
from .permissions import EsMiembroDelProyecto


def usuario_es_miembro(usuario, proyecto):
    return MiembroProyecto.objects.filter(
        usuario=usuario,
        proyecto=proyecto
    ).exists()


class CategoriaLinkViewSet(viewsets.ModelViewSet):
    queryset = CategoriaLink.objects.all()
    serializer_class = CategoriaLinkSerializer
    permission_classes = [IsAuthenticated]


class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated, EsMiembroDelProyecto]

    # Puede ver solo proyectos donde soy miembro
    def get_queryset(self):
        return Proyecto.objects.filter(
            miembros__usuario=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        proyecto = serializer.save(creado_por=self.request.user)

        MiembroProyecto.objects.create(
            usuario=self.request.user,
            proyecto=proyecto,
            rol=MiembroProyecto.Roles.OWNER
        )


class MiembroProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = MiembroProyectoSerializer
    permission_classes = [IsAuthenticated, EsMiembroDelProyecto]

    def get_queryset(self):
        return MiembroProyecto.objects.filter(
            proyecto__miembros__usuario=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        proyecto = serializer.validated_data['proyecto']

        if not usuario_es_miembro(self.request.user, proyecto):
            raise PermissionDenied("No perteneces a este proyecto.")

        serializer.save()

    def perform_update(self, serializer):
        proyecto = serializer.validated_data.get(
            'proyecto',
            serializer.instance.proyecto
        )

        if not usuario_es_miembro(self.request.user, proyecto):
            raise PermissionDenied("No perteneces a este proyecto.")

        serializer.save()


class LinkProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = LinkProyectoSerializer
    permission_classes = [IsAuthenticated, EsMiembroDelProyecto]

    def get_queryset(self):
        return LinkProyecto.objects.filter(
            proyecto__miembros__usuario=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        proyecto = serializer.validated_data['proyecto']

        if not usuario_es_miembro(self.request.user, proyecto):
            raise PermissionDenied("No perteneces a este proyecto.")

        serializer.save(agregado_por=self.request.user)

    def perform_update(self, serializer):
        proyecto = serializer.validated_data.get(
            'proyecto',
            serializer.instance.proyecto
        )

        if not usuario_es_miembro(self.request.user, proyecto):
            raise PermissionDenied("No perteneces a este proyecto.")

        serializer.save()