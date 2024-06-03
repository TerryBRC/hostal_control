from django.urls import path
from . import views

urlpatterns = [
    path('reservas/',views.listar_reservas,name='listar_reservas'),
    path('reservas/crear/',views.crear_reserva,name='crear_reserva'),
    path('reservas/editar/<int:id>',views.editar_reserva,name='editar_reserva'),
    path('reservas/eliminar/<int:id>',views.eliminar_reserva,name='eliminar_reserva'),
]
