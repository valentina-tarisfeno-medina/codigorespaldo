from django.db.models import query
from django.http import HttpResponse
from django.template import Template,Context
from django.template import context
from django.template.loader import get_template
from django.shortcuts import redirect, render
import datetime
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
    
def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    return redirect('home')

def homemacul(request):
    if request.user.is_authenticated:
        return render(request, "homemacul.html")
    return redirect('homemacul')

def homeprovi(request):
    if request.user.is_authenticated:
        return render(request, "homeprovi.html")
    return redirect('homeprovi')

def sede(request):
    return render(request, "sede.html")

def campusmacul(request):
    return render(request, "campusmacul.html")

def campusprovi(request):
    return render(request, "campusprovi.html")

def casacentral(request):
    return render(request, "casacentral.html")

def ingresar_datos(request):
    return render(request, "Ingresar_datos.html")

def ingresar_datosmacul(request):
    return render(request, "Ingresar_datosmacul.html")

def ingresar_datosprovidencia(request):
    return render(request, "Ingresar_datosprovi.html")


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('sede')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('login')   

''' def disponibilidadf(request):
    cantidad_total_de_estacionamientos=30
    can_fun=18
    can_vis=6
    can_res=6
    for i in range(1,19):
        can_fun=can_fun-1
        print("Estacionamiento funcionarios")
        print ("                                               ")
        print(f"Quedan {can_fun} disponibles")
        print (f"Su estacionamiento es el: [{i}]")
        print ("                                               ")
    return render(request, "disponibilidad.html")

def disponibilidadv(request):
    cantidad_total_de_estacionamientos=30
    can_fun=18
    can_vis=6
    can_res=6
    for i in range(19,25):
        can_vis=can_vis-1
        print("Estacionamiento visitantes")
        print ("                                               ")
        print(f"Quedan {can_vis} disponibles")
        print (f"Su estacionamiento es el: [{i}]")
        print ("                                               ")
    return render(request, "disponibilidad.html")

def disponibilidadv(request):
    cantidad_total_de_estacionamientos=30
    can_fun=18
    can_vis=6
    can_res=6
    for i in range(25,31):
        can_res=can_res-1
        print("Estacionamiento Resarvas")
        print ("                                               ")
        print(f"Quedan {can_res} disponibles")
        print (f"Su estacionamiento es el: [{i}]")
        print ("                                               ")
    return render(request, "disponibilidad.html") '''
