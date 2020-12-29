from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, redirect, render
from .models import  Visitante, Visitantemacul, Visitanteprovidencia
from .forms import FormularioVisitante, FormularioVisitantemacul, FormularioVisitanteprovidencia
import datetime
from django.utils import timezone
from django.shortcuts import redirect

def visitante(request):
    if request.method == "POST":
        form = FormularioVisitante(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_visitante', pk=post.id)
    else:
        form = FormularioVisitante()
    return render(request, 'visitante.html', {'form': form})

def mostrar_visitante(request, pk):
    vis = get_object_or_404(Visitante, id=pk)
    contexto = {'Visitante':vis}
    return render(request, "mostrar_registro_vis.html", contexto)

def vis_editar(request, pk):
    vis = get_object_or_404(Visitante, id=pk)
    if request.method == "POST":
        form = FormularioVisitante(request.POST, instance=vis)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_visitante', pk=pk)
    else:
        form = FormularioVisitante(instance=vis)
        return render(request,'visitante.html', {'form': form})

def vis_eliminar(request, pk):
    vis = get_object_or_404(Visitante, id=pk)
    vis.delete()
    return render(request, 'verificar.html', {'vis': vis})

def listar_visitantes(request):
    vis=Visitante.objects.all()
    contexto = {'Visitantes':vis}
    return render(request, "mostrar_visitante.html", contexto)






def visitantemacul(request):
    if request.method == "POST":
        form = FormularioVisitantemacul(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_visitantemacul', pk=post.id)
    else:
        form = FormularioVisitantemacul()
    return render(request, 'visitantemacul.html', {'form': form})

def mostrar_visitantemacul(request, pk):
    visC = get_object_or_404(Visitantemacul, id=pk)
    contexto = {'Visitantemacul':visC }
    return render(request, "mostrar_registro_vismacul.html", contexto)

def vis_editarmacul(request, pk):
    visC  = get_object_or_404(Visitantemacul, id=pk)
    if request.method == "POST":
        form = FormularioVisitantemacul(request.POST, instance=visC )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_visitantemacul', pk=pk)
    else:
        form = FormularioVisitantemacul(instance=visC)
        return render(request,'visitantemacul.html', {'form': form})

def vis_eliminarmacul(request, pk):
    visC  = get_object_or_404(Visitantemacul, id=pk)
    visC .delete()
    return render(request, 'verificarmacul.html', {'vis': visC })

def listar_visitantesmacul(request):
    visC =Visitantemacul.objects.all()
    contexto = {'Visitantesmacul':visC }
    return render(request, "mostrar_visitantemacul.html", contexto)




def visitanteprovidencia(request):
    if request.method == "POST":
        form = FormularioVisitanteprovidencia(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_visitanteprovidencia', pk=post.id)
    else:
        form = FormularioVisitanteprovidencia()
    return render(request, 'visitanteprovi.html', {'form': form})

def mostrar_visitanteprovidencia(request, pk):
    vis = get_object_or_404(Visitanteprovidencia, id=pk)
    contexto = {'Visitanteprovi':vis}
    return render(request, "mostrar_registro_visprovi.html", contexto)

def vis_editarprovidencia(request, pk):
    vis = get_object_or_404(Visitanteprovidencia, id=pk)
    if request.method == "POST":
        form = FormularioVisitanteprovidencia(request.POST, instance=vis)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('mostrar_visitanteprovidencia', pk=pk)
    else:
        form = FormularioVisitanteprovidencia(instance=vis)
        return render(request,'visitanteprovi.html', {'form': form})

def vis_eliminarprovidencia(request, pk):
    vis = get_object_or_404(Visitanteprovidencia, id=pk)
    vis.delete()
    return render(request, 'verificarprovi.html', {'vis': vis})

def listar_visitantesprovidencia(request):
    vis=Visitanteprovidencia.objects.all()
    contexto = {'Visitantesprovi':vis}
    return render(request, "mostrar_visitanteprovi.html", contexto)





