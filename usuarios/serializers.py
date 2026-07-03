# Aca vamos a serializar los datos

from rest_framework import serializers
from .models import UsuarioPersonalizado

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'telefono',
            'is_active'
        )

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UsuarioPersonalizado
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'telefono',
            'password'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = UsuarioPersonalizado(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario