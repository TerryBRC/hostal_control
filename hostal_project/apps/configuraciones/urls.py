from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.listar_config, name='listar_config'),
    path('config/crear/', views.crear_config, name='crear_config'), 
    path('config/editar/<int:id>', views.editar_config,name='editar_config'),
    path('config/eliminar/<int:id>', views.eliminar_config,name='eliminar_config'),
]