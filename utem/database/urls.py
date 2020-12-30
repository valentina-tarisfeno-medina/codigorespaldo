from django.urls import path
from database import views

urlpatterns =[
    path('',                          views.login,                    name='login'),
    path('home/',                     views.home,                     name='home'),
    path('ingresar_datos/',           views.ingresar_datos,           name='ingresar_datos'),
    path('logout/',                   views.logout,                   name='logout')
    
] 