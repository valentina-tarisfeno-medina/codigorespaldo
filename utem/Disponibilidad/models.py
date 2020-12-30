from django.db import models


# Create your models here.

class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    cantidad_estacionamiento=models.IntegerField()
    def __str__(self):
         return self.nombre_sede
    


class Detalle_dispo(models.Model):
    id=models.AutoField(primary_key=True)
    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
    )
    estado=models.CharField(max_length=100)

 


