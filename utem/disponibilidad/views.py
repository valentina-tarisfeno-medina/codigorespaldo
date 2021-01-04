from disponibilidad.models import Disponibilidad
from django.shortcuts import render

# Create your views here.
def checkDisponibilidad(request):
    estacionamientos = Disponibilidad.objects.all()
    contexto = { 'estacionamientos': estacionamientos}
    return render(request, "check_disponibilidad", context=contexto)