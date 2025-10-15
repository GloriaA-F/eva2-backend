from django.shortcuts import render

# Create your views here.
# api_vital/views.py

'''Bloque de Comentarios:
Módulo de Vistas (ViewSets) para la API Salud Vital Ltda.
Implementa el CRUD para cada modelo utilizando ModelViewSet.
Incluye la implementación de filtros avanzados (django-filter)
para campos clave, como médicos por especialidad y consultas por estado.
'''

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import (
    Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento,
    Medicamento, RecetaMedica, DetalleReceta, TipoTratamiento
)
from .serializers import (
    EspecialidadSerializer, PacienteSerializer, MedicoSerializer, 
    ConsultaMedicaSerializer, TratamientoSerializer, MedicamentoSerializer, 
    RecetaMedicaSerializer, DetalleRecetaSerializer, TipoTratamientoSerializer
)


# --- Filtros Personalizados ---
# Un filtro simple para demostrar la capacidad de búsqueda y filtrado
class MedicoFilter(DjangoFilterBackend):
    '''Filtra médicos por ID de especialidad o por apellido (búsqueda).'''
    fields = ['especialidad']
    search_fields = ['rut', 'nombre', 'apellido', 'especialidad__nombre']


class ConsultaFilter(DjangoFilterBackend):
    '''Filtra consultas por médico, paciente o estado (CHOICES).'''
    fields = ['medico', 'paciente', 'estado'] # 'estado' usa los CHOICES
    search_fields = ['motivo_consulta', 'paciente__rut', 'medico__apellido']


# --- Vistas (ViewSets) ---

class EspecialidadViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Especialidades.'''
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre', 'descripcion']


class TipoTratamientoViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Tipos de Tratamiento (Nueva entidad de mejora).'''
    queryset = TipoTratamiento.objects.all()
    serializer_class = TipoTratamientoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Pacientes. Permite filtrar por RUT y buscar por nombre/apellido.'''
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['rut', 'nombre', 'apellido']


class MedicoViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Médicos. Permite filtrar por especialidad.'''
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [MedicoFilter, SearchFilter, OrderingFilter]
    # Filtro aplicado: Se puede filtrar usando ?especialidad=<id>
    # Búsqueda: Se puede buscar por ?search=<termino> en rut, nombre o apellido.
    search_fields = ['rut', 'nombre', 'apellido']


class MedicamentoViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Medicamentos.'''
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nombre_comercial', 'principio_activo']


class ConsultaMedicaViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Consultas Médicas. Permite filtrar por médico, paciente y estado (CHOICES).'''
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer
    filter_backends = [ConsultaFilter, SearchFilter, OrderingFilter]
    # Filtros aplicados: Se puede filtrar usando ?medico=<id>, ?paciente=<id> o ?estado=<PENDIENTE|REALIZADA>
    search_fields = ['diagnostico', 'motivo_consulta']


class TratamientoViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Tratamientos.'''
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consulta', 'tipo'] # Filtrar tratamientos por consulta o tipo


class RecetaMedicaViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Recetas Médicas.'''
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['consulta'] # Filtrar recetas por consulta


class DetalleRecetaViewSet(viewsets.ModelViewSet):
    '''CRUD y listado de Detalles de Receta.'''
    queryset = DetalleReceta.objects.all()
    serializer_class = DetalleRecetaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['receta', 'medicamento']