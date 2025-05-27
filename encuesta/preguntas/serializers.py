from rest_framework import serializers

class RespuestasSerializer(serializers.Serializer):
    respuesta1 = serializers.CharField()
    respuesta2 = serializers.CharField()

class PreguntaSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    texto = serializers.CharField()
    pregunta = serializers.CharField()
    respuestas = RespuestasSerializer()