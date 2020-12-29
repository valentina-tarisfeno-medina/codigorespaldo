from .models import SedeCentro, SedeMacul, SedeProvidencia
from .forms import FormularioSedeCentro, FormularioSedeMacul, FormularioSedeProvidencia
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest
import datetime
from django.utils import timezone

# Create your views here.

def sedecentro(request):
    if request.method == "POST":
        form = FormularioSedeCentro(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sedecentro', pk=post.id)
    else:
        form = FormularioSedeCentro()
    return render(request, 'sedecentro.html', {'form': form})

def mostrar_sedecentro(request, pk):
    sc = get_object_or_404(SedeCentro, id=pk)
    contexto = {'sede_centro':sc}
    return render(request, "mostrar_registro_sedecentro.html", contexto)

def sedecentro_editar(request, pk):
    sc = get_object_or_404(SedeCentro, id=pk)
    if request.method == "POST":
        form = FormularioSedeCentro(request.POST, instance=sc)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sedecentro', pk=pk)
    else:
        form = FormularioSedeCentro(instance=sc)
        return render(request, 'sedecentro.html', {'form': form})

def sedecentro_eliminar(request, pk):
    sc = get_object_or_404(SedeCentro, id=pk)
    sc.delete()
    return render(request, 'verificarcentro.html', {'sc': sc})

def listar_sedecentro(request):
    sc=SedeCentro.objects.all()
    contexto = {'sedecentro':sc}
    return render(request, "mostrarsedecentro.html", contexto)




def sedemacul(request):
    if request.method == "POST":
        form = FormularioSedeMacul(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sedemacul', pk=post.id)
    else:
        form = FormularioSedeMacul()
    return render(request, 'sedemacul.html', {'form': form})

def mostrar_sedemacul(request, pk):
    sm = get_object_or_404(SedeMacul, id=pk)
    contexto = {'sede_macul':sm}
    return render(request, "mostrar_registro_sedemacul.html", contexto)

def sedemacul_editar(request, pk):
    sm = get_object_or_404(SedeMacul, id=pk)
    if request.method == "POST":
        form = FormularioSedeMacul(request.POST, instance=sm)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sedemacul', pk=pk)
    else:
        form = FormularioSedeMacul(instance=sm)
        return render(request, 'sedemacul.html', {'form': form})

def sedemacul_eliminar(request, pk):
    sm = get_object_or_404(SedeMacul, id=pk)
    sm.delete()
    return render(request, 'verificarsedemacul.html', {'sd': sm})

def listar_sedemacul(request):
    sm=SedeMacul.objects.all()
    contexto = {'sedemacul':sm}
    return render(request, "mostrarsedemacul.html", contexto)







def sedeprovidencia(request):
    if request.method == "POST":
        form = FormularioSedeProvidencia(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sedeprovidencia', pk=post.id)
    else:
        form = FormularioSedeProvidencia()
    return render(request, 'sedeprovi.html', {'form': form})

def mostrar_sedeprovidencia(request, pk):
    sp = get_object_or_404(SedeProvidencia, id=pk)
    contexto = {'sedeprovi':sp}
    return render(request, "mostrar_registro_sedeprovi.html", contexto)

def sedeprovidencia_editar(request, pk):
    sp = get_object_or_404(SedeProvidencia, id=pk)
    if request.method == "POST":
        form = FormularioSedeProvidencia(request.POST, instance=sp)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_sedeprovidencia', pk=pk)
    else:
        form = FormularioSedeProvidencia(instance=sp)
        return render(request, 'sedeprovi.html', {'form': form})

def sedeprovidencia_eliminar(request, pk):
    sp = get_object_or_404(SedeProvidencia, id=pk)
    sp.delete()
    return render(request, 'verificarsedeprovi.html', {'sp': sp})

def listar_sedeprovidencia(request):
    sp=SedeProvidencia.objects.all()
    contexto = {'sede_provi':sp}
    return render(request, "mostrarsedeprovi.html", contexto)



def arreglo(request):
    return render(request, "arreglo.html")