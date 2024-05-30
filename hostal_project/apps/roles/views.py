from django.shortcuts import render, get_object_or_404, redirect
from .models import Rol
from .forms import RolForm


def listar_roles(request):
    # Obtener todos los roles desde la base de datos
    roles = Rol.objects.all()
    # Renderizar el template 'roles/listar_roles.html' con la lista de roles
    return render(request, 'listar_roles.html', {'roles': roles})


def crear_rol(request):
    if request.method == 'POST':
        # Si se envió el formulario, procesar los datos
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo rol en la base de datos
            return redirect('listar_roles')  # Redirigir a la lista de roles
    else:
        # Si no se envió el formulario, mostrar el formulario vacío
        form = RolForm()
    # Renderizar el template 'roles/crear_rol.html' con el formulario
    return render(request, 'crear_rol.html', {'form': form})


def ver_rol(request, rol_id):
    # Obtener el rol específico según su ID
    rol = get_object_or_404(Rol, pk=rol_id)
    # Renderizar el template 'roles/ver_rol.html' con los detalles del rol
    return render(request, 'ver_rol.html', {'rol': rol})


def actualizar_rol(request, rol_id):
    # Obtener el rol específico según su ID
    rol = get_object_or_404(Rol, pk=rol_id)
    if request.method == 'POST':
        # Si se envió el formulario, procesar los datos
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()  # Actualizar el rol en la base de datos
            return redirect('listar_roles')  # Redirigir a la lista de roles
    else:
        # Si no se envió el formulario, mostrar el formulario con los datos actuales del rol
        form = RolForm(instance=rol)
    # Renderizar el template 'roles/actualizar_rol.html' con el formulario
    return render(request, 'actualizar_rol.html', {'form': form, 'rol': rol})


def eliminar_rol(request, rol_id):
    # Obtener el rol específico según su ID
    rol = get_object_or_404(Rol, pk=rol_id)
    rol.delete()  # Eliminar el rol de la base de datos
    # Redirigir a la lista de roles después de eliminar
    return redirect('listar_roles')
