from django.urls import path
from database import views

urlpatterns =[
    path('',                          views.login,                    name='login'),
    path('home/',                     views.home,                     name='home'),
    path('homemacul/',                views.homemacul,                name='homemacul'),
    path('homeprovi/',                views.homeprovi,                name='homeprovi'),
    path('ingresar_datos/',           views.ingresar_datos,           name='ingresar_datos'),
    path('ingresar_datosmacul/',      views.ingresar_datosmacul,      name='ingresar_datosmacul'),
    path('ingresar_datosprovidencia/',views.ingresar_datosprovidencia,name='ingresar_datosprovidencia'),
    path('campusmacul/',              views.campusmacul,              name='campusmacul'),
    path('campusprovi/',              views.campusprovi,              name='campusprovi'),
    path('casacentral/',              views.casacentral,              name='casacentral'),
    path('sede/',                     views.sede,                     name='sede'),
    path('logout/',                   views.logout,                   name='logout')
    
] 