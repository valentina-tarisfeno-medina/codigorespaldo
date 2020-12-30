from django.urls import path
from registro import views

urlpatterns =[
    path('registro/',                     views.registro,          name='registro'),
    path('registro_editar/<int:pk>/edit', views.registro_editar,   name='registro_editar'),
    path('registro_eliminar/<int:pk>/',   views.registro_eliminar, name='registro_eliminar'),
    path('listar_registro/all',           views.listar_registro,   name='listar_registro'),
    path('mostrar_registro/<int:pk>/',    views.mostrar_registro,  name='mostrar_registro')
    
] 