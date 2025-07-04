from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from preguntas.views import GuardarContactoView

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de la API",
        default_version='v1',
        description="API de preguntas con JWT",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tucorreo@ejemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('preguntas.urls')),

    # Endpoint personalizado para guardar datos del usuario
    path('api/contacto/', GuardarContactoView.as_view(), name='guardar_contacto'),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger y ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
