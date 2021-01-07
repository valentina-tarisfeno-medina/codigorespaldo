from django.contrib import admin
from .models import Registro, TipoRegistro

# Register your models here.

class RegistroAdmin(admin.ModelAdmin):
    list_display=('nombre','rut', 'patente','sede','usuario','tipo','motivo')

admin.site.register(Registro, RegistroAdmin)


class tipo_registroAdmin(admin.ModelAdmin):
    list_display=('id','nombre_registro')

admin.site.register(TipoRegistro, tipo_registroAdmin)
