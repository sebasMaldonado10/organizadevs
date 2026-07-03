from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegistroUsuarioView, UsuarioActualView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('register/', RegistroUsuarioView.as_view(), name='register'),
    path('me/', UsuarioActualView.as_view(), name='me'),
]

urlpatterns += router.urls