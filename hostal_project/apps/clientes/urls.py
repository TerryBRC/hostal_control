from django.urls import path
from . import views

urlpatterns = [
    path('clientes/',views.listar_clientes,name='listar_clientes'),
    path('clientes/crear',views.crear_cliente,name='crear_cliente'),
    path('clientes/editar/<int:id>',views.editar_cliente,name='editar_cliente'),
    path('clientes/eliminar/<int:id>',views.eliminar_cliente,name='eliminar_cliente'),
]
