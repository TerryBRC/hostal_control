from django.contrib import admin
from django.urls import path, include
from . import views
import django_plotly_dash

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('chart/', views.chart_view, name='chart'),
    path('', include('apps.roles.urls')),
    path('', include('apps.habitaciones.urls')),
    path('',include('apps.usuarios.urls')),
    path('',include('apps.configuraciones.urls')),
    path('',include('apps.clientes.urls')),
    path('',include('apps.reservas.urls')),
]
