# Aca vamos a serializar los datos

from rest_framework import serializers
from .models import LinkProyecto, CategoriaLink, MiembroProyecto, Proyecto, InvitacionProyecto

class CategoriaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaLink
        fields = (
            'id',
            'nombre',
            'descripcion',
            'fecha_creacion'
        )
        read_only_fields = ('id', 'fecha_creacion')

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'id',
            'nombre',
            'descripcion',
            'fecha_entrega',
            'materia',
            'estado',
            'creado_por',
            'fecha_creacion'
        )
        read_only_fields = ('id', 'creado_por', 'fecha_creacion')

class LinkProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkProyecto
        fields = (
            'id',
            'proyecto',
            'titulo',
            'url',
            'descripcion',
            'categoria',
            'agregado_por',
            'fecha_creacion'
        )
        read_only_fields = (
            'id',
            'agregado_por',
            'fecha_creacion'
        )

class MiembroProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiembroProyecto
        fields = (
            'id',
            'usuario',
            'proyecto',
            'rol',
            'fecha_union'
        )
        read_only_fields = ('id', 'fecha_union')

class InvitacionProyectoSerializer(serializers.ModelSerializer):
    proyecto_nombre = serializers.CharField(source="proyecto.nombre", read_only=True)

    class Meta:
        model = InvitacionProyecto
        fields = (
            "id",
            "proyecto",
            "proyecto_nombre",
            "codigo",
            "creado_por",
            "fecha_creacion",
            "usada",
            "usada_por",
            "fecha_uso",
        )
        read_only_fields = (
            "id",
            "codigo",
            "creado_por",
            "fecha_creacion",
            "usada",
            "usada_por",
            "fecha_uso",
        )


class AceptarInvitacionSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=10)

