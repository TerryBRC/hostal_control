from django.db import models


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_rol


class Permiso(models.Model):
    nombre_permiso = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_permiso


class RolPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['rol', 'permiso']

    def __str__(self):
        return f"{self.rol} - {self.permiso}"
