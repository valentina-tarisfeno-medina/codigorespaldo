from django.urls import path
from disponibilidad import views 

urlpatterns = [
    path('check_disponibilidad',  views.check_disponibilidad,   name= "check_disponibilidad"),
    path('listar_disponibilidad', views.listar_disponibilidad,  name= "listar_disponibilidad")
]
