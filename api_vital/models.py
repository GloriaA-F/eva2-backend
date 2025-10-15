from django.db import models

# Create your models here.
# api_vital/models.py

'''Bloque de Comentarios:
Módulo de Modelos de la API para Salud Vital Ltda.
Define la estructura de la base de datos para la gestión
de pacientes, médicos, atenciones, tratamientos y medicamentos.
Incluye mejoras con CHOICES y una nueva tabla (TipoTratamiento).
'''

from django.db import models

# --- CHOICES ---
# Mejoras con CHOICES: Estado de la consulta
ESTADO_CONSULTA_CHOICES = (
    ('PENDIENTE', 'Pendiente'),
    ('CONFIRMADA', 'Confirmada'),
    ('REALIZADA', 'Realizada'),
    ('CANCELADA', 'Cancelada'),
)

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
)


class Especialidad(models.Model):
    '''Entidad para registrar las especialidades médicas.'''
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Especialidades"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    '''Entidad para registrar los datos de los pacientes.'''
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"


class Medico(models.Model):
    '''Entidad para registrar los médicos y su especialidad.'''
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name_plural = "Médicos"

    def __str__(self):
        return f"Dr(a). {self.nombre} {self.apellido} - {self.especialidad.nombre}"


class ConsultaMedica(models.Model):
    '''Entidad para registrar una atención médica o cita.'''
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField()
    motivo_consulta = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    estado = models.CharField(
        max_length=10, 
        choices=ESTADO_CONSULTA_CHOICES, 
        default='PENDIENTE',
        help_text="Estado de la cita: Pendiente, Confirmada, Realizada, Cancelada"
    )

    class Meta:
        ordering = ['-fecha_hora']
        verbose_name_plural = "Consultas Médicas"

    def __str__(self):
        return f"Consulta de {self.paciente} con {self.medico} el {self.fecha_hora.date()}"


# --- NUEVA ENTIDAD/TABLA PARA MEJORA ---
class TipoTratamiento(models.Model):
    '''Nueva Entidad: Clasificación de los tratamientos (e.g., Farmacológico, Fisioterapia, Cirugía).'''
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tipos de Tratamiento"

    def __str__(self):
        return self.nombre


class Tratamiento(models.Model):
    '''Entidad para registrar los tratamientos aplicados a una consulta.'''
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoTratamiento, on_delete=models.PROTECT, help_text="Clasificación del tratamiento.")
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"Tratamiento: {self.nombre} ({self.consulta.paciente})"


class Medicamento(models.Model):
    '''Entidad para registrar los medicamentos disponibles en la clínica.'''
    nombre_comercial = models.CharField(max_length=100, unique=True)
    principio_activo = models.CharField(max_length=100)
    concentracion = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=50) # e.g., Comprimido, Jarabe, Inyectable
    stock = models.IntegerField(default=0)

    class Meta:
        ordering = ['nombre_comercial']

    def __str__(self):
        return f"{self.nombre_comercial} ({self.principio_activo})"


class RecetaMedica(models.Model):
    '''Entidad para registrar las recetas asociadas a una consulta médica.'''
    consulta = models.OneToOneField(ConsultaMedica, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)
    indicaciones_generales = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Recetas Médicas"

    def __str__(self):
        return f"Receta para {self.consulta.paciente} del {self.fecha_emision}"


class DetalleReceta(models.Model):
    '''Entidad para detallar los medicamentos en una receta.'''
    receta = models.ForeignKey(RecetaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)
    dosis = models.CharField(max_length=100)
    frecuencia = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)

    class Meta:
        unique_together = ('receta', 'medicamento')
        verbose_name_plural = "Detalles de Receta"

    def __str__(self):
        return f"{self.medicamento.nombre_comercial} - {self.dosis}"