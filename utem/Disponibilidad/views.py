from .models import Sede
from .forms import FormularioSede
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest
import datetime
from django.utils import timezone

# Create your views here.

def sede(request):
    if request.method == "POST":
        form = FormularioSede(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sede', pk=post.id)
    else:
        form = FormularioSede()
    return render(request, 'sede.html', {'form': form})

def mostrar_sede(request, pk):
    s = get_object_or_404(Sede, id=pk)
    contexto = {'sede':s}
    return render(request, "mostrar_registro_sede.html", contexto)

def sede_editar(request, pk):
    s = get_object_or_404(Sede, id=pk)
    if request.method == "POST":
        form = FormularioSede(request.POST, instance=s)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sede', pk=pk)
    else:
        form = FormularioSede(instance=s)
        return render(request, 'sede.html', {'form': form})

def sede_eliminar(request, pk):
    s = get_object_or_404(Sede, id=pk)
    s.delete()
    return render(request, 'verificar.html', {'s': s})

def listar_sede(request):
    s=Sede.objects.all()
    contexto = {'sedes':s}
    return render(request, "mostrarsede.html", contexto)

