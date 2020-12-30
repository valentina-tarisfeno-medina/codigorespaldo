from django.contrib import admin
from .models import Sede

# Register your models here.

class SedeAdmin(admin.ModelAdmin):
    list_display=('nombre_sede','cantidad_estacionamiento')

admin.site.register(Sede, SedeAdmin)




