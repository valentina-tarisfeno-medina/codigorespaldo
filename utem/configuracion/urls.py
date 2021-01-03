from django.urls import path
from configuracion import views

urlpatterns =[
    path('configuracion/',     views.configuracion,     name='configuracion')
]