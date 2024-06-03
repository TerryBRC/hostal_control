from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table= 'cliente'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
