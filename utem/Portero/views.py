from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from .models import Portero
from .forms import FormularioPortero
import datetime
from django.utils import timezone
from django.shortcuts import redirect

def portero(request):
    if request.method == "POST":
        form = FormularioPortero(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_portero', pk=post.id)
    else:
        form = FormularioPortero()
    return render(request, 'portero.html', {'form': form})

def mostrar_portero(request, pk):
    por = get_object_or_404(Portero, id=pk)
    contexto = {'Portero':por}
    return render(request, "mostrar_registro_por.html", contexto)


def por_editar(request, pk):
    por = get_object_or_404(Portero, id=pk)
    if request.method == "POST":
        form = FormularioPortero(request.POST, instance=por)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_portero', pk=pk)
    else:
        form = FormularioPortero(instance=por)
    return render(request, 'portero.html', {'form': form})

def por_eliminar(request, pk):
    por = get_object_or_404(Portero, id=pk)
    por.delete()
    return render(request, 'verificar.html', {'por': por})

def listar_portero(request):
    por=Portero.objects.all()
    contexto = {'Porteros':por}
    return render(request, "mostrar_portero.html", contexto)