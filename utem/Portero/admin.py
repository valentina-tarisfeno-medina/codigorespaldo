from django.contrib import admin
from .models import  Portero
# Register your models here.

class PorteroAdmin(admin.ModelAdmin):
    list_display=("nombre", "sede")

admin.site.register(Portero, PorteroAdmin)



