from django.urls import path
from Disponibilidad import views

urlpatterns =[
    path('sede/',                    views.sede,               name='sede'),
    path('sede_editar/<int:pk>/edit',views.sede_editar,        name='sede_editar'),
    path('sede_eliminar/<int:pk>/',  views.sede_eliminar,      name='sede_eliminar'),
    path('listar_sede/all',          views.listar_sede,        name='listar_sede'),
    path('mostrar_sede/<int:pk>/',   views.mostrar_sede,       name='mostrar_sede')
    
] 