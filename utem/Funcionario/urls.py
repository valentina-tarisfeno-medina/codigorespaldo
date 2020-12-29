from django.urls import path
from Funcionario import views

urlpatterns =[
    path('funcionario/',                       views.funcionario,                    name='funcionarios'),
    path('fun_editar/<int:pk>/edit',           views.fun_editar,                     name='fun_editar'),
    path('fun_eliminar/<int:pk>/',             views.fun_eliminar,                   name='fun_eliminar'),
    path('funcionario/all',                    views.listar_funcionarios,            name='listar_funcionarios'),
    path('post/<int:pk>/',                     views.mostrar_funcionario,            name='mostrar_funcionario'),

    path('funcionariomacul/',                  views.funcionariomacul,               name='funcionariomacul'),
    path('fun_editarmacul/<int:pk>/edit',      views.fun_editarmacul,                name='fun_editarmacul'),
    path('fun_eliminarmacul/<int:pk>/',        views.fun_eliminarmacul,              name='fun_eliminarmacul'),
    path('funcionariomacul/all',               views.listar_funcionariosmacul,       name='listar_funcionariosmacul'),
    path('postmacul/<int:pk>/',                views.mostrar_funcionariomacul,       name='mostrar_funcionariomacul'),

    path('funcionarioprovidencia/',            views.funcionarioprovidencia,         name='funcionarioprovidencia'),
    path('fun_editarprovidencia/<int:pk>/edit',views.fun_editarprovidencia,          name='fun_editarprovidencia'),
    path('fun_eliminarprovidencia/<int:pk>/',  views.fun_eliminarprovidencia,        name='fun_eliminarprovidencia'),
    path('funcionarioprovidencia/all',         views.listar_funcionariosprovidencia, name='listar_funcionariosprovidencia'),
    path('postprovidencia/<int:pk>/',          views.mostrar_funcionarioprovidencia, name='mostrar_funcionarioprovidencia')
    
] 