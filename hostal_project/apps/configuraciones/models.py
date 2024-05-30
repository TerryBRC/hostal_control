from django.db import models


class ConfiguracionGeneral(models.Model):
    clave = models.CharField(max_length=50, unique=True)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.clave


class ConfiguracionEspecifica(models.Model):
    clave = models.CharField(max_length=50, unique=True)
    valor = models.CharField(max_length=255)

    def __str__(self):
        return self.clave
