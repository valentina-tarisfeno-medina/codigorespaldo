from django.db import models


# Create your models here.

class SedeCentro(models.Model):
    id = models.AutoField(primary_key=True)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Casa central")
    Tipousuario=models.CharField(max_length=100)
    Cantidad_estacionamientos=models.IntegerField()


class SedeMacul(models.Model):
    id = models.AutoField(primary_key=True)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Campus macul")
    Tipousuario=models.CharField(max_length=100)
    Cantidad_estacionamientos=models.IntegerField()

class SedeProvidencia(models.Model):
    id = models.AutoField(primary_key=True)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Campus providencia")
    Tipousuario=models.CharField(max_length=100)
    Cantidad_estacionamientos=models.IntegerField()

 


