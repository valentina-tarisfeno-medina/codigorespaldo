from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from .models import Portero, Porteromacul, Porteroprovidencia
from .forms import FormularioPortero,FormularioPorteromacul, FormularioPorteroprovidencia
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





def porteromacul(request):
    if request.method == "POST":
        form = FormularioPorteromacul(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_porteromacul', pk=post.id)
    else:
        form = FormularioPorteromacul()
    return render(request, 'porteromacul.html', {'form': form})

def mostrar_porteromacul(request, pk):
    por = get_object_or_404(Porteromacul, id=pk)
    contexto = {'PorteroM':por}
    return render(request, "mostrar_registro_pormacul.html", contexto)

def por_editarmacul(request, pk):
    por = get_object_or_404(Porteromacul, id=pk)
    if request.method == "POST":
        form = FormularioPorteromacul(request.POST, instance=por)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_porteromacul', pk=pk)
    else:
        form = FormularioPorteromacul(instance=por)
    return render(request, 'porteromacul.html', {'form': form})

def por_eliminarmacul(request, pk):
    por = get_object_or_404(Porteromacul, id=pk)
    por.delete()
    return render(request, 'eliminarmacul.html', {'por': por})

def listar_porteromacul(request):
    por=Porteromacul.objects.all()
    contexto = {'PorterosM':por}
    return render(request, "mostrar_porteromacul.html", contexto)





def porteroprovidencia(request):
    if request.method == "POST":
        form = FormularioPorteroprovidencia(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_porteroprovidencia', pk=post.id)
    else:
        form = FormularioPorteroprovidencia()
    return render(request, 'porteroprovi.html', {'form': form})

def mostrar_porteroprovidencia(request, pk):
    por = get_object_or_404(Porteroprovidencia, id=pk)
    contexto = {'PorteroP':por}
    return render(request, "mostrar_registro_porprovi.html", contexto)

def por_editarprovidencia(request, pk):
    por = get_object_or_404(Porteroprovidencia, id=pk)
    if request.method == "POST":
        form = FormularioPorteroprovidencia(request.POST, instance=por)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_porteroprovidencia', pk=pk)
    else:
        form = FormularioPorteroprovidencia(instance=por)
    return render(request, 'porteroprovi.html', {'form': form})

def por_eliminarprovidencia(request, pk):
    por = get_object_or_404(Porteroprovidencia, id=pk)
    por.delete()
    return render(request, 'eliminarprovi.html', {'por': por})

def listar_porteroprovidencia(request):
    por=Porteroprovidencia.objects.all()
    contexto = {'PorterosP':por}
    return render(request, "mostrar_porteroprovi.html", contexto)
