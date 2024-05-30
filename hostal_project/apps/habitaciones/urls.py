# apps/habitaciones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URLs para Habitacion
    path('habitaciones/', views.listar_habitaciones, name='listar_habitaciones'),
    path('habitaciones/crear/', views.crear_habitacion, name='crear_habitacion'),
    path('habitaciones/<int:pk>/', views.ver_habitacion, name='ver_habitacion'),
    path('habitaciones/<int:pk>/editar/',
         views.editar_habitacion, name='editar_habitacion'),
    path('habitaciones/<int:pk>/eliminar/',
         views.eliminar_habitacion, name='eliminar_habitacion'),

    # URLs para TipoHabitacion
    path('tipo_habitaciones/', views.listar_tipo_habitaciones,
         name='listar_tipo_habitaciones'),
    path('tipo_habitaciones/crear/', views.crear_tipo_habitacion,
         name='crear_tipo_habitacion'),
    path('tipo_habitaciones/<int:pk>/',
         views.ver_tipo_habitacion, name='ver_tipo_habitacion'),
    path('tipo_habitaciones/<int:pk>/editar/',
         views.editar_tipo_habitacion, name='editar_tipo_habitacion'),
    path('tipo_habitaciones/<int:pk>/eliminar/',
         views.eliminar_tipo_habitacion, name='eliminar_tipo_habitacion'),
]
