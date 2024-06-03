from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('', include('apps.roles.urls')),
    path('', include('apps.habitaciones.urls')),
    path('',include('apps.usuarios.urls')),
]
