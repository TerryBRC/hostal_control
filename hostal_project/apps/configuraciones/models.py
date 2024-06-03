from django.db import models


class ConfiguracionGeneral(models.Model):
    clave = models.CharField(max_length=50, unique=True,verbose_name='Clave')
    valor = models.CharField(max_length=255,verbose_name='Valor')
    class Meta:
        db_table = 'configsys'

    def __str__(self):
        return self.clave
