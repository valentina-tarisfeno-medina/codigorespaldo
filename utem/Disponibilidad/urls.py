from django.urls import path
from Disponibilidad import views

urlpatterns =[
    path('sedecentro/',                          views.sedecentro,               name='sedecentro'),
    path('sedecentro_editar/<int:pk>/edit',      views.sedecentro_editar,        name='sedecentro_editar'),
    path('sedecentro_eliminar/<int:pk>/',        views.sedecentro_eliminar,      name='sedecentro_eliminar'),
    path('listar_sedecentro/all',                views.listar_sedecentro,        name='listar_sedecentro'),
    path('mostrar_sedecentro/<int:pk>/',         views.mostrar_sedecentro,       name='mostrar_sedecentro'),


    path('sedemacul/',                           views.sedemacul,                name='sedemacul'),
    path('sedemacul_editar/<int:pk>/edit',       views.sedemacul_editar,         name='sedemacul_editar'),
    path('sedemacul_eliminar/<int:pk>/',         views.sedemacul_eliminar,       name='sedemacul_eliminar'),
    path('listar_sedemacul/all',                 views.listar_sedemacul,         name='listar_sedemacul'),
    path('mostrar_sedemacul/<int:pk>/',          views.mostrar_sedemacul,        name='mostrar_sedemacul'),


    path('sedeprovidencia/',                     views.sedeprovidencia,          name='sedeprovidencia'),
    path('sedeprovidencia_editar/<int:pk>/edit', views.sedeprovidencia_editar,   name='sedeprovidencia_editar'),
    path('sedeprovidencia_eliminar/<int:pk>/',   views.sedeprovidencia_eliminar, name='sedeprovidencia_eliminar'),
    path('listar_sedeprovidencia/all',           views.listar_sedeprovidencia,   name='listar_sedeprovidencia'),
    path('mostrar_sedeprovidencia/<int:pk>/',    views.mostrar_sedeprovidencia,  name='mostrar_sedeprovidencia'),
    
] 