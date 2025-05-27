from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId
from django.db import models

def get_collection():
    client = MongoClient(settings.MONGODB_URI)
    db = client.get_default_database()  # Usa 'University' desde la URI
    return db['Question']

def get_contact_collection():
    client = MongoClient(settings.MONGODB_URI)
    db = client.get_default_database()
    return db['usuarios_interesados']

class Pregunta(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

    @staticmethod
    def get_all():
        return list(get_collection().find())

    @staticmethod
    def get_by_id(id):
        return get_collection().find_one({'_id': ObjectId(id)})

    @staticmethod
    def create(data):
        return get_collection().insert_one(data).inserted_id

class UsuarioInteresado:
    @staticmethod
    def guardar(data):
        return get_contact_collection().insert_one(data)

def get_respuestas_collection():
    client = MongoClient(settings.MONGODB_URI)
    db = client.get_default_database()
    return db['Respuestas']  # ← nueva colección

class RespuestaUsuario:
    @staticmethod
    def guardar_respuesta(data):
        collection = get_respuestas_collection()
        return collection.insert_one(data).inserted_id
    
class EncuestaUsuario:
    @staticmethod
    def guardar_respuesta(data):
        return get_encuesta_collection().insert_one(data).inserted_id    