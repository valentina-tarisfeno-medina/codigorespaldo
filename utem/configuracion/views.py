from django.shortcuts import render

# Create your views here.

def configuracioncentral(request):
    return render(request, "configuracioncentro.html")

def configuracionmacul(request):
    return render(request, "configuracionmacul.html")

def configuracionprovidencia(request):
    return render(request, "configuracionprovi.html")