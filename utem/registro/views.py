from disponibilidad.functions import asignarEstacionamiento
from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from .models import Registro
from .forms import FormularioRegistro
import datetime
from django.utils import timezone
from django.shortcuts import redirect
import numpy as np 
from disponibilidad.models import Disponibilidad


def registro(request):
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            asignarEstacionamiento(post, post.sede )
            return redirect('mostrar_registro', pk=post.id)
    else:
        form = FormularioRegistro()
    return render(request, 'registro.html', {'form': form})

def mostrar_registro(request, pk):
    fun = get_object_or_404(Registro, id=pk)
    estacionamiento = Disponibilidad.objects.get(registro = fun) 
    contexto = {'registro':fun, 'estacionamiento': estacionamiento}
    return render(request, "mostrar_registro.html", contexto)

def registro_editar(request, pk):
    fun = get_object_or_404(Registro, id=pk)
    if request.method == "POST":
        form = FormularioRegistro(request.POST, instance=fun)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_registro', pk=pk)
    else:
        form = FormularioRegistro(instance=fun)
        return render(request, 'registro.html', {'form': form})

def registro_eliminar(request, pk):
    fun = get_object_or_404(Registro, id=pk)
    fun.delete()
    return render(request, 'verificar.html', {'fun': fun})

def listar_registro(request):
    fun=Registro.objects.all()
    contexto = {'registros':fun}
    return render(request, "listar_registro.html", contexto)