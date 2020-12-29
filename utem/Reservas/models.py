from django.db import models

# Create your models here.

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_reserva=models.CharField(max_length=30)
    Rut_reserva=models.CharField(max_length=200)
    Usuario_Reserva=models.CharField(max_length=30)
    Fecha_Reserva=models.DateField()
    Cantidad_horas=models.PositiveIntegerField()
    Patente=models.CharField(max_length=30)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default="Casa central")
    Motivo=models.CharField(max_length=1000)


class Reservamacul(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_reserva=models.CharField(max_length=30)
    Rut_reserva=models.CharField(max_length=200)
    Usuario_Reserva=models.CharField(max_length=30)
    Fecha_Reserva=models.DateField()
    Cantidad_horas=models.PositiveIntegerField()
    Patente=models.CharField(max_length=30)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default="Campus macul")
    Motivo=models.CharField(max_length=1000)



class Reservaprovidencia(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_reserva=models.CharField(max_length=30)
    Rut_reserva=models.CharField(max_length=200)
    Usuario_Reserva=models.CharField(max_length=30)
    Fecha_Reserva=models.DateField()
    Cantidad_horas=models.PositiveIntegerField()
    Patente=models.CharField(max_length=30)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default="Campus providencia")
    Motivo=models.CharField(max_length=1000)