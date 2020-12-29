from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Sede(models.Model):
    id = models.AutoField(primary_key=True)
    campus_macul=models.CharField(max_length=200)
    campus_providencia=models.CharField(max_length=200)
    casa_central=models.CharField(max_length=6)
    cantidad_estacionamiento = models.CharField(max_length=1000)