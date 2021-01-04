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
    day  = timezone.now()
    hour = timezone.now()
    #formatedHour = hour.strftime("%Y/%m/%d %H:%M:%S")
    formatedDay  = day.strftime("%Y/%m/%d")
    formatedHour = hour.strftime("%H:%M:%S")
    dia = models.CharField(max_length=50, default=formatedDay)

    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    rut=models.CharField(max_length=200)
    patente=models.CharField(max_length=6)
    sede = models.ForeignKey(Sede,on_delete=models.SET_NULL, null=True, blank=True)
    usuario=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    fecha_entrada = models.CharField(max_length=50, default=formatedHour)
    fecha_salida = models.CharField(max_length=50, default=formatedHour)
    tipo=models.ForeignKey(TipoRegistro, on_delete=models.SET_NULL, null= True, blank= True)
    motivo = models.CharField(max_length=1000)



