# SaludVitalProject/urls.py

'''Bloque de Comentarios:
Módulo de URLs de Nivel de Proyecto para Salud Vital Ltda.
Configura las rutas principales, incluyendo el administrador de DRF,
la documentación (Swagger/OpenAPI) y las rutas de la API/Gestión.
'''

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Ruta al administrador de Django
    path('admin/', admin.site.urls),
    
    # Sistema de Documentación
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Rutas para los ENDPOINT de la API (DRF)
    path('api/v1/', include('api_vital.urls')),
    
    # REQUISITO: Ruta hacia la GESTIÓN (TEMPLATES/HTML).
    # Esta línea ahora captura la ruta raíz ('/')
    path('', include('api_vital.urls')),
]