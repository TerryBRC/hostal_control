from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.listar_roles, name='listar_roles'),
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/<int:rol_id>/', views.ver_rol, name='ver_rol'),
    path('roles/<int:rol_id>/actualizar/', views.actualizar_rol, name='actualizar_rol'),
    path('roles/<int:rol_id>/eliminar/', views.eliminar_rol, name='eliminar_rol'),
]
