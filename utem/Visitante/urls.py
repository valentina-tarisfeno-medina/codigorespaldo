from django.urls import path
from Visitante import views

urlpatterns =[
    path('visitante/',                 views.visitante,           name='visitante'),
    path('vis_editar/<int:pk>/',       views.vis_editar,          name='vis_editar'),
    path('vis_eliminar/<int:pk>/',     views.vis_eliminar,        name='vis_eliminar'),
    path('visitante/all',              views.listar_visitantes,   name='listar_visitantes'),
    path('mostrar_visitante/<int:pk>/',views.mostrar_visitante ,  name='mostrar_visitante'),

    path('visitantemacul/',                      views.visitantemacul,           name='visitantemacul'),
    path('vis_editarmacul/<int:pk>/',            views.vis_editarmacul,          name='vis_editarmacul'),
    path('vis_eliminarmacul/<int:pk>/',          views.vis_eliminarmacul,        name='vis_eliminarmacul'),
    path('visitantemacul/all',                   views.listar_visitantesmacul,   name='listar_visitantesmacul'),
    path('mostrar_visitantemacul/<int:pk>/',     views.mostrar_visitantemacul,  name='mostrar_visitantemacul'),


    path('visitanteprovidencia/',                 views.visitanteprovidencia,           name='visitanteprovidencia'),
    path('vis_editarprovidencia/<int:pk>/',       views.vis_editarprovidencia,          name='vis_editarprovidencia'),
    path('vis_eliminarprovidencia/<int:pk>/',     views.vis_eliminarprovidencia,        name='vis_eliminarprovidencia'),
    path('visitanteprovidencia/all',              views.listar_visitantesprovidencia,   name='listar_visitantesprovidencia'),
    path('mostrar_visitanteprovidencia/<int:pk>/',views.mostrar_visitanteprovidencia,  name='mostrar_visitanteprovidencia'),
]