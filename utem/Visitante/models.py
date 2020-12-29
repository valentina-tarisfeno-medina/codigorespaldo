from django.db import models

# Create your models here.

class Visitante(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Rut=models.CharField(max_length=200)
    Patente=models.CharField(max_length=30)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Casa central")
    Fecha_Ingreso=models.DateTimeField(auto_now_add=True)
    Fecha_Salida=models.DateField()
    Motivo=models.CharField(max_length=1000)

class Visitantemacul(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Rut=models.CharField(max_length=200)
    Patente=models.CharField(max_length=30)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Campus macul")
    Fecha_Ingreso=models.DateTimeField(auto_now_add=True)
    Fecha_Salida=models.DateField()
    Motivo=models.CharField(max_length=1000)

class Visitanteprovidencia(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Rut=models.CharField(max_length=200)
    Patente=models.CharField(max_length=30)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Campus providencia")
    Fecha_Ingreso=models.DateTimeField(auto_now_add=True)
    Fecha_Salida=models.DateField()
    Motivo=models.CharField(max_length=1000)


