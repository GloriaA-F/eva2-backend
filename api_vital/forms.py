# api_vital/forms.py

'''Bloque de Comentarios:
Módulo de Formularios de Django.
Define los formularios (ModelForm) usados por las vistas basadas en Templates (HTML)
para la captura de datos (Crear y Actualizar) de todas las entidades del modelo.
'''

from django import forms
from .models import (
    Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, 
    Medicamento, RecetaMedica, DetalleReceta, TipoTratamiento
)

# ----------------- ENTIDADES BÁSICAS Y AUXILIARES -----------------

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class TipoTratamientoForm(forms.ModelForm):
    class Meta:
        model = TipoTratamiento
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            # Facilita la selección de la fecha en el template
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}), 
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'

# ----------------- ENTIDADES DE ATENCIÓN MÉDICA -----------------

class ConsultaMedicaForm(forms.ModelForm):
    class Meta:
        model = ConsultaMedica
        fields = '__all__'
        widgets = {
            # Permite ingresar fecha y hora fácilmente
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
        }
        
class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = ['consulta', 'indicaciones_generales']
        
class DetalleRecetaForm(forms.ModelForm):
    class Meta:
        model = DetalleReceta
        fields = '__all__'