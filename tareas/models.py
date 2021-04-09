from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Tarea(models.Model):
    ALTA = '1'
    NORMAL = '2'
    BAJA = '3'
   
    PRIORIDAD_TAREA = (
        (ALTA, 'Alta'),
        (NORMAL, 'Normal'),
        (BAJA, 'Baja'),
    )

    nombre = models.CharField(max_length=100, help_text="Nombre de la tarea")
    descripcion = models.TextField(help_text="Descripción de la tarea")
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    prioridad = models.CharField(
        max_length=20,
        choices=PRIORIDAD_TAREA,
        default='2',
        blank=True,
        help_text="Prioridad de la tarea"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tarea.nombre