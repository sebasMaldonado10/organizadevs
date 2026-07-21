from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CategoriaLink, LinkProyecto, MiembroProyecto, Proyecto, InvitacionProyecto
from .serializers import (
    CategoriaLinkSerializer,
    LinkProyectoSerializer,
    MiembroProyectoSerializer,
    ProyectoSerializer,
    InvitacionProyectoSerializer,
    AceptarInvitacionSerializer
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

class InvitacionProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = InvitacionProyectoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InvitacionProyecto.objects.filter(
            proyecto__miembros__usuario=self.request.user
        ).distinct()

    def perform_create(self, serializer):
        proyecto = serializer.validated_data["proyecto"]

        if not usuario_es_miembro(self.request.user, proyecto):
            raise PermissionDenied("No perteneces a este proyecto.")

        serializer.save(creado_por=self.request.user)


class AceptarInvitacionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AceptarInvitacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        codigo = serializer.validated_data["codigo"].upper()

        try:
            invitacion = InvitacionProyecto.objects.get(codigo=codigo)
        except InvitacionProyecto.DoesNotExist:
            return Response(
                {"detail": "Código de invitación inválido."},
                status=status.HTTP_404_NOT_FOUND
            )

        if invitacion.usada:
            return Response(
                {"detail": "Esta invitación ya fue usada."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if usuario_es_miembro(request.user, invitacion.proyecto):
            return Response(
                {"detail": "Ya perteneces a este proyecto."},
                status=status.HTTP_400_BAD_REQUEST
            )

        MiembroProyecto.objects.create(
            usuario=request.user,
            proyecto=invitacion.proyecto,
            rol=MiembroProyecto.Roles.MIEMBRO
        )

        invitacion.marcar_como_usada(request.user)

        return Response(
            {
                "detail": "Te uniste al proyecto correctamente.",
                "proyecto_id": invitacion.proyecto.id,
                "proyecto_nombre": invitacion.proyecto.nombre,
            },
            status=status.HTTP_200_OK
        )