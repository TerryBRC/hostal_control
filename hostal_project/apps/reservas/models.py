from django.db import models
from apps.clientes.models import Cliente
from apps.habitaciones.models import Habitacion


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    numero_huespedes = models.IntegerField()
    estado_reserva = models.CharField(max_length=20, choices=[
        ('Activo', 'Activo'),
        ('Pendiente', 'Pendiente'),
        ('Cancelado', 'Cancelado'),
    ])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nombre} {self.cliente.apellido}"
