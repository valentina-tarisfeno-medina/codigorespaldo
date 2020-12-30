from django.contrib import admin
from .models import Registro

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Registro, RegistroAdmin)
