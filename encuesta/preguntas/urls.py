from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect 
from rest_framework.routers import DefaultRouter
from .views import PreguntaViewSet

router = DefaultRouter()
router.register(r'preguntas', PreguntaViewSet, basename='pregunta')
urlpatterns = [
   
    path('admin/', admin.site.urls),
       path('', include(router.urls)),
   
    
]