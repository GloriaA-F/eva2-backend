# api_vital/urls.py

'''Bloque de Comentarios:
Módulo de URLs de la Aplicación API Vital.
Define las rutas (endpoints) para el acceso a los datos de las entidades
utilizando el router de Django REST Framework.
'''

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    EspecialidadViewSet, PacienteViewSet, MedicoViewSet, ConsultaMedicaViewSet, 
    TratamientoViewSet, MedicamentoViewSet, RecetaMedicaViewSet, 
    DetalleRecetaViewSet, TipoTratamientoViewSet
)

router = DefaultRouter()

# Definición de las rutas (endpoints) para cada ViewSet (entidad)
router.register(r'especialidades', EspecialidadViewSet) # CRUD Especialidad
router.register(r'tipos-tratamiento', TipoTratamientoViewSet) # CRUD Tipo Tratamiento
router.register(r'pacientes', PacienteViewSet) # CRUD Paciente
router.register(r'medicos', MedicoViewSet) # CRUD Medico
router.register(r'medicamentos', MedicamentoViewSet) # CRUD Medicamento
router.register(r'consultas-medicas', ConsultaMedicaViewSet) # CRUD consulta_medica
router.register(r'tratamientos', TratamientoViewSet) # CRUD tratamiento
router.register(r'recetas-medicas', RecetaMedicaViewSet) # CRUD receta_medica
router.register(r'detalles-receta', DetalleRecetaViewSet) # CRUD DetalleReceta

urlpatterns = [
    # Incluye todas las rutas generadas por el router (GET, POST, PUT, DELETE)
    path('', include(router.urls)),
]

# api_vital/urls.py

'''Bloque de Comentarios:
Módulo de URLs de la Aplicación API Vital.
Define las rutas (endpoints) para la API (DRF) y las rutas de gestión
basadas en Templates (HTML), cumpliendo el requisito del CRUD fuera del admin.
'''

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    EspecialidadViewSet, PacienteViewSet, MedicoViewSet, ConsultaMedicaViewSet, 
    TratamientoViewSet, MedicamentoViewSet, RecetaMedicaViewSet, 
    DetalleRecetaViewSet, TipoTratamientoViewSet
)
from .template_views import (
    EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView,
    PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView,
    MedicoListView, MedicoCreateView, MedicoUpdateView, MedicoDeleteView,
    MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView,
    ConsultaMedicaListView, ConsultaMedicaCreateView, ConsultaMedicaUpdateView, ConsultaMedicaDeleteView,
    TratamientoListView, TratamientoCreateView, TratamientoUpdateView, TratamientoDeleteView,
    RecetaMedicaListView, RecetaMedicaCreateView, RecetaMedicaUpdateView, RecetaMedicaDeleteView,
    DetalleRecetaListView, DetalleRecetaCreateView, DetalleRecetaUpdateView, DetalleRecetaDeleteView,
    TipoTratamientoListView, TipoTratamientoCreateView, TipoTratamientoUpdateView, TipoTratamientoDeleteView,
    IndexView
)

router = DefaultRouter()

# Rutas para los ENDPOINTS de la API (DRF)
router.register(r'especialidades', EspecialidadViewSet) 
router.register(r'tipos-tratamiento', TipoTratamientoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'consultas-medicas', ConsultaMedicaViewSet)
router.register(r'tratamientos', TratamientoViewSet)
router.register(r'recetas-medicas', RecetaMedicaViewSet)
router.register(r'detalles-receta', DetalleRecetaViewSet)


urlpatterns = [
    # Ruta principal para la GESTIÓN (TEMPLATES)
    path('', IndexView.as_view(), name='index_vital'), 

    # --- RUTA PARA LOS ENDPOINTS DE LA API (v1) ---
    path('endpoints/', include(router.urls)), 
    
    # --- RUTAS DE GESTIÓN (TEMPLATES) PARA EL CRUD ---
    
    # Especialidad
    path('gestion/especialidades/', EspecialidadListView.as_view(), name='especialidad_list'),
    path('gestion/especialidades/crear/', EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('gestion/especialidades/editar/<int:pk>/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('gestion/especialidades/eliminar/<int:pk>/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    # Paciente
    path('gestion/pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('gestion/pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    path('gestion/pacientes/editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('gestion/pacientes/eliminar/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_delete'),

    # Medico
    path('gestion/medicos/', MedicoListView.as_view(), name='medico_list'),
    path('gestion/medicos/crear/', MedicoCreateView.as_view(), name='medico_create'),
    path('gestion/medicos/editar/<int:pk>/', MedicoUpdateView.as_view(), name='medico_update'),
    path('gestion/medicos/eliminar/<int:pk>/', MedicoDeleteView.as_view(), name='medico_delete'),

    # Medicamento
    path('gestion/medicamentos/', MedicamentoListView.as_view(), name='medicamento_list'),
    path('gestion/medicamentos/crear/', MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('gestion/medicamentos/editar/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('gestion/medicamentos/eliminar/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),

    # Consulta Medica
    path('gestion/consultas/', ConsultaMedicaListView.as_view(), name='consultamedica_list'),
    path('gestion/consultas/crear/', ConsultaMedicaCreateView.as_view(), name='consultamedica_create'),
    path('gestion/consultas/editar/<int:pk>/', ConsultaMedicaUpdateView.as_view(), name='consultamedica_update'),
    path('gestion/consultas/eliminar/<int:pk>/', ConsultaMedicaDeleteView.as_view(), name='consultamedica_delete'),

    # Tratamiento
    path('gestion/tratamientos/', TratamientoListView.as_view(), name='tratamiento_list'),
    path('gestion/tratamientos/crear/', TratamientoCreateView.as_view(), name='tratamiento_create'),
    path('gestion/tratamientos/editar/<int:pk>/', TratamientoUpdateView.as_view(), name='tratamiento_update'),
    path('gestion/tratamientos/eliminar/<int:pk>/', TratamientoDeleteView.as_view(), name='tratamiento_delete'),
    
    # Receta Medica
    path('gestion/recetas/', RecetaMedicaListView.as_view(), name='recetamedica_list'),
    path('gestion/recetas/crear/', RecetaMedicaCreateView.as_view(), name='recetamedica_create'),
    path('gestion/recetas/editar/<int:pk>/', RecetaMedicaUpdateView.as_view(), name='recetamedica_update'),
    path('gestion/recetas/eliminar/<int:pk>/', RecetaMedicaDeleteView.as_view(), name='recetamedica_delete'),
    
    # Detalle Receta (Auxiliar)
    path('gestion/detalles-receta/', DetalleRecetaListView.as_view(), name='detallereceta_list'),
    path('gestion/detalles-receta/crear/', DetalleRecetaCreateView.as_view(), name='detallereceta_create'),
    path('gestion/detalles-receta/editar/<int:pk>/', DetalleRecetaUpdateView.as_view(), name='detallereceta_update'),
    path('gestion/detalles-receta/eliminar/<int:pk>/', DetalleRecetaDeleteView.as_view(), name='detallereceta_delete'),
    
    # Tipos de Tratamiento (Auxiliar)
    path('gestion/tipos-tratamiento/', TipoTratamientoListView.as_view(), name='tipotratamiento_list'),
    path('gestion/tipos-tratamiento/crear/', TipoTratamientoCreateView.as_view(), name='tipotratamiento_create'),
    path('gestion/tipos-tratamiento/editar/<int:pk>/', TipoTratamientoUpdateView.as_view(), name='tipotratamiento_update'),
    path('gestion/tipos-tratamiento/eliminar/<int:pk>/', TipoTratamientoDeleteView.as_view(), name='tipotratamiento_delete'),
]