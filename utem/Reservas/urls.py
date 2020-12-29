from django.urls import path
from Reservas import views

urlpatterns =[
    path('reserva/',                            views.reserva,                     name='reservas'),
    path('res_editar/<int:pk>/edit',            views.res_editar,                  name='res_editar'),
    path('res_eliminar/<int:pk>/',              views.res_eliminar,                name='res_eliminar'),
    path('reserva/all',                         views.listar_reservas,             name='listar_reservas'),
    path('mostrar_reserva/<int:pk>/',           views.mostrar_reserva,             name='mostrar_reserva'), 

    path('reservamacul/',                       views.reservamacul,               name='reservasmacul'),
    path('res_editarmacul/<int:pk>/edit',       views.res_editarmacul,            name='res_editarmacul'),
    path('res_eliminarmacul/<int:pk>/',         views.res_eliminarmacul,          name='res_eliminarmacul'),
    path('reservamacul/all',                    views.listar_reservasmacul,       name='listar_reservasmacul'),
    path('mostrar_reservamacul/<int:pk>/',      views.mostrar_reservamacul,       name='mostrar_reservamacul'),

    path('reservaprovidencia/',                 views.reservaprovidencia,         name='reservasprovidencia'),
    path('res_editarprovidencia/<int:pk>/edit', views.res_editarprovidencia,      name='res_editarprovidencia'),
    path('res_eliminarprovidencia/<int:pk>/',   views.res_eliminarprovidencia,    name='res_eliminarprovidencia'),
    path('reservaprovidencia/all',              views.listar_reservasprovidencia, name='listar_reservasprovidencia'),
    path('mostrar_reservaprovidencia/<int:pk>/',views.mostrar_reservaprovidencia, name='mostrar_reservaprovidencia')
    
]