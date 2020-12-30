from Disponibilidad.models import Sede
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    rut=models.CharField(max_length=200)
    patente=models.CharField(max_length=6)
    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
    )
    usuario=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    fecha_entrada=models.DateTimeField(auto_now_add=True)
    fecha_salida=models.DateTimeField()
    tipo=models.CharField(max_length=1000)
    motivo = models.CharField(max_length=1000)


class tipo_registro(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_registro=models.CharField(max_length=1000)
