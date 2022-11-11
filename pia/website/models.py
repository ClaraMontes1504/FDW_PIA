from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length = 50 )
    direccion = models.CharField(max_length = 60)

    def __str__(self):
        return self.nombre
        