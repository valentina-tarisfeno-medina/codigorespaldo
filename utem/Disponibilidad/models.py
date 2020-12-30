from django.db import models


# Create your models here.

class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    campus_macul = models.CharField(max_length=100)
    campus_providencia = models.CharField(max_length=100)
    casa_central=models.CharField(max_length=100)
    cantidad_estacionamiento=models.IntegerField()


class Detalle_dispo(models.Model):
    id=models.AutoField(primary_key=True)
    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
    )
    estado=models.CharField(max_length=100)

 


