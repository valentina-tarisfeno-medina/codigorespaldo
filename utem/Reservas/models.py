from django.db import models
from sede.models import Sede

# Create your models here.

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_reserva=models.CharField(max_length=30)
    rut_reserva=models.CharField(max_length=200)
    usuario_reserva=models.CharField(max_length=30)
    patente=models.CharField(max_length=30)
    fecha_entrada=models.DateTimeField()
    fecha_salida=models.DateTimeField()
    cantidad_horas=models.PositiveIntegerField()
    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
    )
    motivo=models.CharField(max_length=1000)


