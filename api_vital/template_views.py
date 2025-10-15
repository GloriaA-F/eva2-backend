# api_vital/template_views.py

'''Bloque de Comentarios:
Módulo de Vistas basadas en Templates (HTML) para el CRUD.
Utiliza Clases de Vistas Genéricas (CBV) para implementar
las operaciones de crear, listar, actualizar y eliminar para
cada entidad, cumpliendo con el requisito de no usar el admin de DRF.
'''

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import (
    Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, 
    Medicamento, RecetaMedica, DetalleReceta, TipoTratamiento
)
from .forms import (
    EspecialidadForm, PacienteForm, MedicoForm, ConsultaMedicaForm, 
    TratamientoForm, MedicamentoForm, RecetaMedicaForm, DetalleRecetaForm,
    TipoTratamientoForm
)

# Definimos el patrón de implementación para todas las entidades

# --- 1. Especialidad ---
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'api_vital/especialidad_list.html'
    context_object_name = 'especialidades'
class EspecialidadCreateView(CreateView):
    model = Especialidad; form_class = EspecialidadForm; template_name = 'api_vital/especialidad_form.html'; success_url = reverse_lazy('especialidad_list')
class EspecialidadUpdateView(UpdateView):
    model = Especialidad; form_class = EspecialidadForm; template_name = 'api_vital/especialidad_form.html'; success_url = reverse_lazy('especialidad_list')
class EspecialidadDeleteView(DeleteView):
    model = Especialidad; template_name = 'api_vital/especialidad_confirm_delete.html'; success_url = reverse_lazy('especialidad_list')

# --- 2. TipoTratamiento (Nueva entidad de mejora) ---
class TipoTratamientoListView(ListView):
    model = TipoTratamiento
    template_name = 'api_vital/tipotratamiento_list.html'
    context_object_name = 'tipos_tratamiento'
class TipoTratamientoCreateView(CreateView):
    model = TipoTratamiento; form_class = TipoTratamientoForm; template_name = 'api_vital/tipotratamiento_form.html'; success_url = reverse_lazy('tipotratamiento_list')
class TipoTratamientoUpdateView(UpdateView):
    model = TipoTratamiento; form_class = TipoTratamientoForm; template_name = 'api_vital/tipotratamiento_form.html'; success_url = reverse_lazy('tipotratamiento_list')
class TipoTratamientoDeleteView(DeleteView):
    model = TipoTratamiento; template_name = 'api_vital/tipotratamiento_confirm_delete.html'; success_url = reverse_lazy('tipotratamiento_list')

# --- 3. Paciente ---
class PacienteListView(ListView):
    model = Paciente; template_name = 'api_vital/paciente_list.html'; context_object_name = 'pacientes'
class PacienteCreateView(CreateView):
    model = Paciente; form_class = PacienteForm; template_name = 'api_vital/paciente_form.html'; success_url = reverse_lazy('paciente_list')
class PacienteUpdateView(UpdateView):
    model = Paciente; form_class = PacienteForm; template_name = 'api_vital/paciente_form.html'; success_url = reverse_lazy('paciente_list')
class PacienteDeleteView(DeleteView):
    model = Paciente; template_name = 'api_vital/paciente_confirm_delete.html'; success_url = reverse_lazy('paciente_list')

# --- 4. Medico ---
class MedicoListView(ListView):
    model = Medico; template_name = 'api_vital/medico_list.html'; context_object_name = 'medicos'
class MedicoCreateView(CreateView):
    model = Medico; form_class = MedicoForm; template_name = 'api_vital/medico_form.html'; success_url = reverse_lazy('medico_list')
class MedicoUpdateView(UpdateView):
    model = Medico; form_class = MedicoForm; template_name = 'api_vital/medico_form.html'; success_url = reverse_lazy('medico_list')
class MedicoDeleteView(DeleteView):
    model = Medico; template_name = 'api_vital/medico_confirm_delete.html'; success_url = reverse_lazy('medico_list')

# --- 5. Medicamento ---
class MedicamentoListView(ListView):
    model = Medicamento; template_name = 'api_vital/medicamento_list.html'; context_object_name = 'medicamentos'
class MedicamentoCreateView(CreateView):
    model = Medicamento; form_class = MedicamentoForm; template_name = 'api_vital/medicamento_form.html'; success_url = reverse_lazy('medicamento_list')
class MedicamentoUpdateView(UpdateView):
    model = Medicamento; form_class = MedicamentoForm; template_name = 'api_vital/medicamento_form.html'; success_url = reverse_lazy('medicamento_list')
class MedicamentoDeleteView(DeleteView):
    model = Medicamento; template_name = 'api_vital/medicamento_confirm_delete.html'; success_url = reverse_lazy('medicamento_list')

# --- 6. ConsultaMedica (Requiere manejar Foráneas) ---
class ConsultaMedicaListView(ListView):
    model = ConsultaMedica; template_name = 'api_vital/consultamedica_list.html'; context_object_name = 'consultas'
class ConsultaMedicaCreateView(CreateView):
    model = ConsultaMedica; form_class = ConsultaMedicaForm; template_name = 'api_vital/consultamedica_form.html'; success_url = reverse_lazy('consultamedica_list')
class ConsultaMedicaUpdateView(UpdateView):
    model = ConsultaMedica; form_class = ConsultaMedicaForm; template_name = 'api_vital/consultamedica_form.html'; success_url = reverse_lazy('consultamedica_list')
class ConsultaMedicaDeleteView(DeleteView):
    model = ConsultaMedica; template_name = 'api_vital/consultamedica_confirm_delete.html'; success_url = reverse_lazy('consultamedica_list')

# --- 7. Tratamiento ---
class TratamientoListView(ListView):
    model = Tratamiento; template_name = 'api_vital/tratamiento_list.html'; context_object_name = 'tratamientos'
class TratamientoCreateView(CreateView):
    model = Tratamiento; form_class = TratamientoForm; template_name = 'api_vital/tratamiento_form.html'; success_url = reverse_lazy('tratamiento_list')
class TratamientoUpdateView(UpdateView):
    model = Tratamiento; form_class = TratamientoForm; template_name = 'api_vital/tratamiento_form.html'; success_url = reverse_lazy('tratamiento_list')
class TratamientoDeleteView(DeleteView):
    model = Tratamiento; template_name = 'api_vital/tratamiento_confirm_delete.html'; success_url = reverse_lazy('tratamiento_list')

# --- 8. RecetaMedica ---
class RecetaMedicaListView(ListView):
    model = RecetaMedica; template_name = 'api_vital/recetamedica_list.html'; context_object_name = 'recetas'
class RecetaMedicaCreateView(CreateView):
    model = RecetaMedica; form_class = RecetaMedicaForm; template_name = 'api_vital/recetamedica_form.html'; success_url = reverse_lazy('recetamedica_list')
class RecetaMedicaUpdateView(UpdateView):
    model = RecetaMedica; form_class = RecetaMedicaForm; template_name = 'api_vital/recetamedica_form.html'; success_url = reverse_lazy('recetamedica_list')
class RecetaMedicaDeleteView(DeleteView):
    model = RecetaMedica; template_name = 'api_vital/recetamedica_confirm_delete.html'; success_url = reverse_lazy('recetamedica_list')
    
# --- 9. DetalleReceta (Auxiliar de Receta) ---
class DetalleRecetaListView(ListView):
    model = DetalleReceta; template_name = 'api_vital/detallereceta_list.html'; context_object_name = 'detalles_receta'
class DetalleRecetaCreateView(CreateView):
    model = DetalleReceta; form_class = DetalleRecetaForm; template_name = 'api_vital/detallereceta_form.html'; success_url = reverse_lazy('detallereceta_list')
class DetalleRecetaUpdateView(UpdateView):
    model = DetalleReceta; form_class = DetalleRecetaForm; template_name = 'api_vital/detallereceta_form.html'; success_url = reverse_lazy('detallereceta_list')
class DetalleRecetaDeleteView(DeleteView):
    model = DetalleReceta; template_name = 'api_vital/detallereceta_confirm_delete.html'; success_url = reverse_lazy('detallereceta_list')

# Vista de Índice para navegar entre los módulos
class IndexView(ListView):
    template_name = 'api_vital/index.html'
    queryset = [] # No necesita datos del modelo