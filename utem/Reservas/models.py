from sede.models import Sede
from django.db import models

# Create your models here.

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_reserva=models.CharField(max_length=30)
    rut_reserva=models.CharField(max_length=200)
    usuario_reserva=models.CharField(max_length=30)
    patente=models.CharField(max_length=30)
    fecha_reserva=models.DateTimeField()
    cantidad_horas=models.PositiveIntegerField()
    sede = models.ForeignKey(Sede,on_delete=models.SET_NULL, null=True, blank=True)
    motivo=models.CharField(max_length=1000)

    def __str__(self):
            return self.nombre_reserva

