from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Pregunta, UsuarioInteresado
from .serializers import PreguntaSerializer
from bson import ObjectId

class PreguntaViewSet(viewsets.ViewSet):
    def list(self, request):
        preguntas = Pregunta.get_all()
        for pregunta in preguntas:
            pregunta['_id'] = str(pregunta['_id'])
        return Response(preguntas)

class GuardarContactoView(APIView):
    def post(self, request):
        data = request.data
        try:
            UsuarioInteresado.guardar(data)
            return Response({"mensaje": "Datos guardados correctamente."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
