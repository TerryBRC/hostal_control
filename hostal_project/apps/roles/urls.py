from django.urls import path
from . import views

urlpatterns = [
    #urls de roles
    path('roles/', views.listar_roles, name='listar_roles'),
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/<int:rol_id>/', views.ver_rol, name='ver_rol'),
    path('roles/<int:rol_id>/actualizar/',views.actualizar_rol, name='actualizar_rol'),
    path('roles/<int:rol_id>/eliminar/',views.eliminar_rol, name='eliminar_rol'),
    #urls de permisos
    path('permisos/', views.listar_permisos, name='listar_permisos'),
    path('permisos/crear/', views.crear_permiso, name='crear_permiso'),
    path('permisos/<int:permiso_id>/', views.ver_permiso, name='ver_permiso'),
    path('permisos/<int:permiso_id>/actualizar/',views.actualizar_permiso, name='actualizar_permiso'),
    path('permisos/<int:permiso_id>/eliminar/',views.eliminar_permiso, name='eliminar_permiso'),
]
