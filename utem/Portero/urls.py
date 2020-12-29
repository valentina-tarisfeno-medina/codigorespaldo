from django.urls import path
from Portero import views

urlpatterns =[
    path('portero/',                           views.portero,                    name='porteros'),
    path('por_editar/<int:pk>/edit',           views.por_editar,                 name='por_editar'),
    path('por_eliminar/<int:pk>/',             views.por_eliminar,               name='por_eliminar'),
    path('portero/all',                        views.listar_portero,             name='listar_portero'),
    path('portero/<int:pk>/',                  views.mostrar_portero,            name='mostrar_portero'), 


    path('porteromacul/',                      views.porteromacul,               name='porterosmacul'),
    path('por_editarmacul/<int:pk>/edit',      views.por_editarmacul,            name='por_editarmacul'),
    path('por_eliminarmacul/<int:pk>/',        views.por_eliminarmacul,          name='por_eliminarmacul'),
    path('porteromacul/all',                   views.listar_porteromacul,        name='listar_porteromacul'),
    path('porteromacul/<int:pk>/',             views.mostrar_porteromacul,       name='mostrar_porteromacul'),

    path('porteroprovidencia/',                views.porteroprovidencia,         name='porterosprovidencia'),
    path('por_editarprovidencia/<int:pk>/edit',views.por_editarprovidencia,      name='por_editarprovidencia'),
    path('por_eliminarprovidencia/<int:pk>/',  views.por_eliminarprovidencia,    name='por_eliminarprovidencia'),
    path('porteroprovidencia/all',             views.listar_porteroprovidencia,  name='listar_porteroprovidencia'),
    path('porteroprovidencia/<int:pk>/',       views.mostrar_porteroprovidencia, name='mostrar_porteroprovidencia')
]