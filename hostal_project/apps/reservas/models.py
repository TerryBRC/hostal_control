from django.db import models
from apps.clientes.models import Cliente
from apps.habitaciones.models import Habitacion


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,verbose_name='Cliente')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE,verbose_name='Habitación')
    fecha_entrada = models.DateField(verbose_name='Fecha de Entrada')
    fecha_salida = models.DateField(verbose_name='Fecha de Salida')
    numero_huespedes = models.IntegerField(verbose_name='Total Huéspedes')
    estado_reserva = models.CharField(max_length=20, choices=[
        ('Activo', 'Activo'),
        ('Pendiente', 'Pendiente'),
        ('Cancelado', 'Cancelado'),
    ],verbose_name='Estado de la Reserva')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Reservas'
        db_table='reserva'

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nombre} {self.cliente.apellido}"
