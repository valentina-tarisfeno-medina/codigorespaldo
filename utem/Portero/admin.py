from django.contrib import admin
from .models import  Portero,Porteromacul,Porteroprovidencia

# Register your models here.

class PorteroAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Sede")

admin.site.register(Portero, PorteroAdmin)

class PorteromaculAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Sede")

admin.site.register(Porteromacul, PorteromaculAdmin)

class PorteroprovidenciaAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Sede")

admin.site.register(Porteroprovidencia, PorteroprovidenciaAdmin)

