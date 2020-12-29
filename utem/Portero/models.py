from django.db import models

# Create your models here.

class Portero(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Rut=models.CharField(max_length=200)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Casa central")
    Incio_Turno=models.DateTimeField(auto_now_add=True)
    Fin_Turno=models.DateField()


class Porteromacul(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Rut=models.CharField(max_length=200)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Campus macul")
    Incio_Turno=models.DateTimeField(auto_now_add=True)
    Fin_Turno=models.DateField()



class Porteroprovidencia(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=30)
    Rut=models.CharField(max_length=200)
    SEDE_CHOICES=(('Casa central','Casa central'),
                  ('Campus macul','Campus macul'),
                  ('Campus providencia','Campus providencia'),)
    Sede = models.CharField(max_length=100, choices=SEDE_CHOICES, default= "Campus providencia")
    Incio_Turno=models.DateTimeField(auto_now_add=True)
    Fin_Turno=models.DateField()