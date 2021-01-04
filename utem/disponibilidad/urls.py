from django.urls import path
from disponibilidad import views 

urlpatterns = [
    path('checkDisponibilidad', views.checkDisponibilidad, name= "checkDisponibilidad")
]
