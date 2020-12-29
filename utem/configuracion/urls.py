from django.urls import path
from configuracion import views

urlpatterns =[
    path('configuracioncentral/',     views.configuracioncentral,     name='configuracioncentral'),
    path('configuracionmacul/',       views.configuracionmacul,       name='configuracionmacul'),
    path('configuracionprovidencia/', views.configuracionprovidencia, name='configuracionprovidencia')
]