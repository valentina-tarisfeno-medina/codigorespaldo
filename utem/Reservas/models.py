from django.db import models

# Create your models here.

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_reserva=models.CharField(max_length=30)
    rut_reserva=models.CharField(max_length=200)
    usuario_reserva=models.CharField(max_length=30)
    patente=models.CharField(max_length=30)
    fecha_entrada=models.DateField()
    fecha_salida=models.DateField()
    cantidad_horas=models.PositiveIntegerField()
    sede = models.CharField(max_length=100)
    motivo=models.CharField(max_length=1000)


