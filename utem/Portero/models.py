from sede.models import Sede
from django.db import models

# Create your models here.

class Portero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    rut=models.CharField(max_length=200)
    sede = models.CharField(max_length=200)
    incio_Turno=models.DateTimeField(auto_now_add=True)
    fin_Turno=models.DateField()