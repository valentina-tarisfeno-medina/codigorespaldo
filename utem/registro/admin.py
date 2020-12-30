from django.contrib import admin
from .models import Registro, tipo_registro

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
    list_display=('nombre','rut', 'patente','sede','usuario','fecha_salida','tipo','motivo')

admin.site.register(Registro, RegistroAdmin)


class tipo_registroAdmin(admin.ModelAdmin):
    list_display=('id','nombre_registro')

admin.site.register(tipo_registro, tipo_registroAdmin)
