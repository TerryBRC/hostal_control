from django.db import models
from apps.roles.models import Rol

class Usuario(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    correo_electronico = models.EmailField(unique=True,verbose_name='E-mail')
    contrasena = models.CharField(max_length=255,verbose_name='Contraseña')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE,verbose_name='Rol')
    fecha_creacion = models.DateTimeField(auto_now_add=True,null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True,null=True)
    activo = models.BooleanField(default=True,verbose_name="Activo")
    class Meta:
        db_table= 'usuario'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
