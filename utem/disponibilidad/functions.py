from django.db.models.deletion import RestrictedError
from .models import Disponibilidad
from registro.models import Registro
from Reservas.models import Reserva
from sede.models import Sede

def asignarEstacionamiento(registro, sede):
    ocupados = Disponibilidad.objects.filter(registro__sede = sede)
    num_ocupados = len(ocupados)
    print(num_ocupados)
    if(num_ocupados == sede.cantidad_estacionamiento):
        print("Todos ocupados")
        return False; 
    else:
        print("Asignando estacionamiento")
        for espacio in range(1, sede.cantidad_estacionamiento):
            print("Espacio"+ str(espacio))
            if str(espacio) not in ocupados.values_list('numero_estacionamiento', flat=True):
                estacionamiento = Disponibilidad(registro= registro, numero_estacionamiento= espacio)
                return estacionamiento.save()

def asignarEstacionamientor(reserva, sede):
    ocupados = Disponibilidad.objects.filter(reserva__sede = sede)
    num_ocupados = len(ocupados) 
    print(num_ocupados)
    if(num_ocupados == sede.cantidad_estacionamiento):
        print("Todos ocupados")
        return False;
    else:
        print("Asignando estacionamiento")
        for espacio in range(1, sede.cantidad_estacionamiento):
            print("Espacio"+ str(espacio))
            if str(espacio) not in ocupados.values_list('numero_estacionamiento', flat=True):
                estacionamiento = Disponibilidad(reserva= reserva, numero_estacionamiento= espacio)
                return estacionamiento.save()