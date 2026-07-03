from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado


class UsuarioPersonalizadoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Datos personalizados', {
            'fields': ('telefono',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Datos personalizados', {
            'fields': ('email', 'telefono')
        }),
    )

    list_display = ('username', 'email', 'telefono', 'is_staff', 'is_active')


admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)
