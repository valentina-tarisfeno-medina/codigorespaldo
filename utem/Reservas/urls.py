from django.urls import path
from Reservas import views

urlpatterns =[
    path('reserva/',                            views.reserva,                     name='reservas'),
    path('res_editar/<int:pk>/edit',            views.res_editar,                  name='res_editar'),
    path('res_eliminar/<int:pk>/',              views.res_eliminar,                name='res_eliminar'),
    path('reserva/all',                         views.listar_reservas,             name='listar_reservas'),
    path('mostrar_reserva/<int:pk>/',           views.mostrar_reserva,             name='mostrar_reserva')
    
]