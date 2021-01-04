from disponibilidad.functions import asignarEstacionamientor
from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from .models import Reserva 
from .forms import  FormularioReserva 
import datetime
from django.utils import timezone
from django.shortcuts import redirect
from disponibilidad.models import Disponibilidad

# Create your views here.

def reserva(request):
    if request.method == "POST":
        form = FormularioReserva(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            asignarEstacionamientor(post, post.sede)
            return redirect('mostrar_reserva', pk=post.id)
    else:
        form = FormularioReserva()
    return render(request, 'reservas.html', {'form': form})

def mostrar_reserva(request, pk):
    res = get_object_or_404(Reserva, id=pk)
    estacionamiento = Disponibilidad.objects.get(reserva = res) 
    contexto = {'Reserva':res, 'estacionamiento': estacionamiento}
    return render(request, "mostrar_registro_res.html", contexto)

def res_editar(request, pk):
    res = get_object_or_404(Reserva, id=pk)
    if request.method == "POST":
        form = FormularioReserva(request.POST, instance=res)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_reserva', pk=pk)
    else:
        form = FormularioReserva(instance=res)
    return render(request, 'reservas.html', {'form': form})

def res_eliminar(request, pk):
    res = get_object_or_404(Reserva, id=pk)
    res.delete()
    return render(request, 'verificar.html', {'res': res})

def listar_reservas(request):
    res=Reserva.objects.all()
    contexto = {'Reservas':res}
    return render(request, "mostrar_reserva.html", contexto)