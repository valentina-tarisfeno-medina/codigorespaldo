from django.contrib import admin
from .models import Reserva

# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display=("nombre_reserva", "patente", "sede")
    search_fields=("nombre_reserva", "patente", "sede")
    list_fields=("nombre_reserva", "patente", "sede")

admin.site.register(Reserva, ReservaAdmin)

