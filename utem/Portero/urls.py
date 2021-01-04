from django.urls import path
from Portero import views

urlpatterns =[
    path('portero/',                           views.portero,                    name='porteros'),
    path('por_editar/<int:pk>/edit',           views.por_editar,                 name='por_editar'),
    path('por_eliminar/<int:pk>/',             views.por_eliminar,               name='por_eliminar'),
    path('portero/all',                        views.listar_portero,             name='listar_portero'),
    path('portero/<int:pk>/',                  views.mostrar_portero,            name='mostrar_portero')

]