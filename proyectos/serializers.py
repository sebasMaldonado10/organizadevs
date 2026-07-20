# Aca vamos a serializar los datos

from rest_framework import serializers
from .models import LinkProyecto, CategoriaLink, MiembroProyecto, Proyecto

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

