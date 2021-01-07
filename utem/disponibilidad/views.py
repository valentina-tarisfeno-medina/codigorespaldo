from disponibilidad.models import Disponibilidad
from django.shortcuts import render

# Create your views here.
def check_disponibilidad(request):
    estacionamientos = Disponibilidad.objects.all()
    contexto = { 'estacionamientos': estacionamientos}
    return render(request, "check_disponibilidad.html", context=contexto)

def listar_disponibilidad(request):
    dis=Disponibilidad.objects.all()
    contexto = {'disponibilidad':dis}
    return render(request, "listar_disponibilidad.html", contexto)