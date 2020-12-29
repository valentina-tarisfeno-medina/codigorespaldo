from django.contrib import admin
from .models import Funcionario, Funcionariomacul, Funcionarioprovi

# Register your models here.

class FuncionarioAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Funcionario, FuncionarioAdmin)

class FuncionariomaculAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Funcionariomacul, FuncionariomaculAdmin)

class FuncionarioproviAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Patente", "Sede")

admin.site.register(Funcionarioprovi, FuncionarioproviAdmin)
