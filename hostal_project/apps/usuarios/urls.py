from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'), 
    path('usuario/eliminar/<int:id>', views.eliminar_usuario,name='eliminar_usuario'),
    path('usuario/editar/<int:id>', views.editar_usuario,name='editar_usuario')

]