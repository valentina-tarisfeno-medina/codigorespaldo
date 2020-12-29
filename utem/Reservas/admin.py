from django.contrib import admin
from .models import Reserva, Reservamacul, Reservaprovidencia

# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display=("Nombre_reserva", "Patente", "Sede")

admin.site.register(Reserva, ReservaAdmin)

class ReservamaculAdmin(admin.ModelAdmin):
    list_display=("Nombre_reserva", "Patente", "Sede")

admin.site.register(Reservamacul, ReservamaculAdmin)


class ReservaprovidenciaAdmin(admin.ModelAdmin):
    list_display=("Nombre_reserva", "Patente", "Sede")

admin.site.register(Reservaprovidencia, ReservaprovidenciaAdmin)