from django.contrib import admin
from .models import  Visitante, Visitantemacul, Visitanteprovidencia

# Register your models here.

class VisitanteAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Visitante, VisitanteAdmin)

class VisitantemaculAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Visitantemacul, VisitantemaculAdmin)

class VisitanteproviAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Visitanteprovidencia, VisitanteproviAdmin)