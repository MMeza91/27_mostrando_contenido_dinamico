from django.db import models

# Create your models here.
class Listado(models.Model):
    nombre = models.CharField('nombre', max_length=40)
    edad = models.CharField('edad', max_length=40)

    def __str__(self):
        return f'{self.nombre}'