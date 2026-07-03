from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaLinkViewSet, 
    ProyectoViewSet, 
    MiembroProyectoViewSet, 
    LinkProyectoViewSet
)

router = DefaultRouter()

router.register(r'categorias', CategoriaLinkViewSet, basename='categorias')
router.register(r'proyectos', ProyectoViewSet, basename='proyectos')
router.register(r'miembros', MiembroProyectoViewSet, basename='miembros')
router.register(r'links', LinkProyectoViewSet, basename='links')

urlpatterns = router.urls