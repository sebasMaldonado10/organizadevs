from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import UsuarioPersonalizado
from .serializers import UsuarioSerializer, RegistroUsuarioSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class RegistroUsuarioView(generics.CreateAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [AllowAny]

class UsuarioActualView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    

