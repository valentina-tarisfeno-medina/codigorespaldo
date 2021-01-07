from Reservas.models import Reserva
from registro.models import Registro
from Reservas.models import Reserva
from django.db import models

# Create your models here.
class Disponibilidad(models.Model):
    id = models.AutoField(primary_key=True)
    registro = models.ForeignKey(Registro, on_delete=models.SET_NULL, null=True)
    '''reserva = models.ForeignKey(Reserva, on_delete=models.SET_NULL, null=True)'''
    numero_estacionamiento = models.CharField(max_length=10)
    ocupado = models.BooleanField(default= True)