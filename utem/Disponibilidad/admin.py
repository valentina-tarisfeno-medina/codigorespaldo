from django.contrib import admin
from .models import Sede, Detalle_dispo

# Register your models here.

class SedeAdmin(admin.ModelAdmin):
    list_display=('campus_macul','campus_providencia','casa_central','cantidad_estacionamiento')

admin.site.register(Sede, SedeAdmin)

class Detalle_dispoAdmin(admin.ModelAdmin):
    list_display=('sede','estado')

admin.site.register(Detalle_dispo, Detalle_dispoAdmin)


