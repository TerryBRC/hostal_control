from django.db import models


class TipoHabitacion(models.Model):
    tipo_habitacion = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_habitacion


class Habitacion(models.Model):
    numero_habitacion = models.CharField(max_length=10)
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE)
    capacidad_maxima = models.IntegerField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.numero_habitacion
