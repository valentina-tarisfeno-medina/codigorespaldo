from django.urls import path
from configuracion import views

urlpatterns =[
    path('configuracioncentral/',     views.configuracioncentral,     name='configuracioncentral')
]