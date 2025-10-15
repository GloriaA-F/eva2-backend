# api_vital/serializers.py

'''Bloque de Comentarios:
Módulo de Serializers para la API Salud Vital Ltda.
Define la forma en que los datos de los modelos son serializados (convertidos a JSON)
y deserializados (convertidos a objetos Python) para la comunicación con el cliente.
'''

from rest_framework import serializers
from .models import (
    Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento,
    Medicamento, RecetaMedica, DetalleReceta, TipoTratamiento
)

# ----------------- ENTIDADES INDEPENDIENTES -----------------

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__' # CRUD completo

class TipoTratamientoSerializer(serializers.ModelSerializer):
    # Serializer para la nueva tabla de mejora
    class Meta:
        model = TipoTratamiento
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    # El campo 'sexo' utilizará automáticamente los CHOICES definidos en el modelo.
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoSerializer(serializers.ModelSerializer):
    # Muestra el nombre de la especialidad en la lista/detalle
    especialidad_nombre = serializers.ReadOnlyField(source='especialidad.nombre')
    
    class Meta:
        model = Medico
        fields = '__all__'
        read_only_fields = ['especialidad_nombre'] # Para evitar que se pueda modificar desde aquí

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


# ----------------- ENTIDADES DEPENDIENTES -----------------

class RecetaMedicaSerializer(serializers.ModelSerializer):
    # Se utiliza OneToOneField, por lo que se serializa la consulta
    class Meta:
        model = RecetaMedica
        fields = '__all__'

class DetalleRecetaSerializer(serializers.ModelSerializer):
    # Mostrar el nombre del medicamento en lugar del ID
    medicamento_nombre = serializers.ReadOnlyField(source='medicamento.nombre_comercial')
    
    class Meta:
        model = DetalleReceta
        fields = '__all__'
        read_only_fields = ['medicamento_nombre']

class TratamientoSerializer(serializers.ModelSerializer):
    # Muestra el nombre del tipo de tratamiento
    tipo_nombre = serializers.ReadOnlyField(source='tipo.nombre')
    
    class Meta:
        model = Tratamiento
        fields = '__all__'
        read_only_fields = ['tipo_nombre']

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    # Muestra los nombres del paciente y médico
    paciente_nombre = serializers.ReadOnlyField(source='paciente.__str__')
    medico_nombre = serializers.ReadOnlyField(source='medico.__str__')
    
    class Meta:
        model = ConsultaMedica
        fields = '__all__'
        read_only_fields = ['paciente_nombre', 'medico_nombre']