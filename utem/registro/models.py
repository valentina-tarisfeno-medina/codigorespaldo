from sede.models import Sede
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TipoRegistro(models.Model):
    id=models.AutoField(primary_key=True)
    nombre_registro=models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.nombre_registro
# Create your models here.

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    rut=models.CharField(max_length=200)
    patente=models.CharField(max_length=6)
    sede = models.ForeignKey(Sede,on_delete=models.SET_NULL, null=True, blank=True)
    usuario=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    tipo=models.ForeignKey(TipoRegistro, on_delete=models.SET_NULL, null= True, blank= True)
    motivo = models.CharField(max_length=1000)



