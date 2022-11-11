from django.db import models


# Create your models here.
class  Producto(models.Model):
    descripcion = models.CharField(max_length= 80)
    presentacion = models.CharField(max_length=80)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion