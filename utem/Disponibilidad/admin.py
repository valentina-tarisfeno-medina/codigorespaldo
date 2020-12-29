from django.contrib import admin
from .models import SedeCentro, SedeMacul, SedeProvidencia

# Register your models here.

class SedeCentroAdmin(admin.ModelAdmin):
    list_display=("Sede", "Cantidad_estacionamientos")

admin.site.register(SedeCentro, SedeCentroAdmin)

class SedeMaculAdmin(admin.ModelAdmin):
    list_display=("Sede", "Cantidad_estacionamientos")

admin.site.register(SedeMacul, SedeMaculAdmin)

class SedeProvidenciaAdmin(admin.ModelAdmin):
    list_display=("Sede", "Cantidad_estacionamientos")

admin.site.register(SedeProvidencia, SedeProvidenciaAdmin)
