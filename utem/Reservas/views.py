from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from .models import Reserva, Reservamacul, Reservaprovidencia
from .forms import  FormularioReserva, FormularioReservamacul, FormularioReservaprovidencia
import datetime
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def reserva(request):
    if request.method == "POST":
        form = FormularioReserva(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_reserva', pk=post.id)
    else:
        form = FormularioReserva()
    return render(request, 'reservas.html', {'form': form})

def mostrar_reserva(request, pk):
    res = get_object_or_404(Reserva, id=pk)
    contexto = {'Reserva':res}
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






def reservamacul(request):
    if request.method == "POST":
        form = FormularioReservamacul(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_reservamacul', pk=post.id)
    else:
        form = FormularioReservamacul()
    return render(request, 'reservasmacul.html', {'form': form})

def mostrar_reservamacul(request, pk):
    res = get_object_or_404(Reservamacul, id=pk)
    contexto = {'ReservaM':res}
    return render(request, "mostrar_registro_resmacul.html", contexto)

def res_editarmacul(request, pk):
    res = get_object_or_404(Reservamacul, id=pk)
    if request.method == "POST":
        form = FormularioReservamacul(request.POST, instance=res)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_reservamacul', pk=pk)
    else:
        form = FormularioReservamacul(instance=res)
    return render(request, 'reservasmacul.html', {'form': form})

def res_eliminarmacul(request, pk):
    res = get_object_or_404(Reservamacul, id=pk)
    res.delete()
    return render(request, 'verificarmacul.html', {'res': res})

def listar_reservasmacul(request):
    res=Reservamacul.objects.all()
    contexto = {'ReservasM':res}
    return render(request, "mostrar_reservamacul.html", contexto)







def reservaprovidencia(request):
    if request.method == "POST":
        form = FormularioReservaprovidencia(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_reservaprovidencia', pk=post.id)
    else:
        form = FormularioReservaprovidencia()
    return render(request, 'reservasprovi.html', {'form': form})

def mostrar_reservaprovidencia(request, pk):
    res = get_object_or_404(Reservaprovidencia, id=pk)
    contexto = {'ReservaM':res}
    return render(request, "mostrar_registro_resprovi.html", contexto)

def res_editarprovidencia(request, pk):
    res = get_object_or_404(Reservaprovidencia, id=pk)
    if request.method == "POST":
        form = FormularioReservaprovidencia(request.POST, instance=res)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_reservaprovidencia', pk=pk)
    else:
        form = FormularioReservaprovidencia(instance=res)
    return render(request, 'reservasprovi.html', {'form': form})

def res_eliminarprovidencia(request, pk):
    res = get_object_or_404(Reservaprovidencia, id=pk)
    res.delete()
    return render(request, 'verificarprovi.html', {'res': res})

def listar_reservasprovidencia(request):
    res=Reservaprovidencia.objects.all()
    contexto = {'ReservasM':res}
    return render(request, "mostrar_reservaprovi.html", contexto)