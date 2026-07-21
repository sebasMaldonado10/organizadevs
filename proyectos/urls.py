from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaLinkViewSet,
    ProyectoViewSet,
    MiembroProyectoViewSet,
    LinkProyectoViewSet,
    InvitacionProyectoViewSet,
    AceptarInvitacionView,
)

router = DefaultRouter()

router.register(r'categorias', CategoriaLinkViewSet, basename='categorias')
router.register(r'proyectos', ProyectoViewSet, basename='proyectos')
router.register(r'miembros', MiembroProyectoViewSet, basename='miembros')
router.register(r'links', LinkProyectoViewSet, basename='links')
router.register(r'invitaciones', InvitacionProyectoViewSet, basename='invitaciones')

urlpatterns = [
    path(
        'aceptar-invitacion/',
        AceptarInvitacionView.as_view(),
        name='aceptar-invitacion'
    ),
]

urlpatterns += router.urls