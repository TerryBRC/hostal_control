from django.shortcuts import render, get_object_or_404, redirect
from .models import Rol, Permiso, RolPermiso
from .forms import RolForm, PermisoForm, RolPermisoForm

# CRUD ROLES


def listar_roles(request):
    # Obtener todos los roles desde la base de datos
    roles = Rol.objects.all()
    # Renderizar el template 'roles/listar_roles.html' con la lista de roles
    headers = ['ID', 'Nombre', 'Descripcion']  # define the headers
    return render(request, 'listar_roles.html', {'roles': roles,'headers':headers})


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

# CRUD PERMISOS


def listar_permisos(request):
    permisos = Permiso.objects.all()
    headers = ["Permiso","Descripción"]
    return render(request, 'listar_permisos.html', {'permisos': permisos,'headers':headers})


def crear_permiso(request):
    if request.method == 'POST':
        form = PermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_permisos')
    else:
        form = PermisoForm()
    return render(request, 'crear_permiso.html', {'form': form})


def ver_permiso(request, permiso_id):
    permiso = get_object_or_404(Permiso, pk=permiso_id)
    return render(request, 'ver_permiso.html', {'permiso': permiso})


def actualizar_permiso(request, permiso_id):
    permiso = get_object_or_404(Permiso, pk=permiso_id)
    if request.method == 'POST':
        form = PermisoForm(request.POST, instance=permiso)
        if form.is_valid():
            form.save()
            return redirect('listar_permisos')
    else:
        form = PermisoForm(instance=permiso)
    return render(request, 'actualizar_permiso.html', {'form': form, 'permiso': permiso})


def eliminar_permiso(request, permiso_id):
    # Obtener el rol específico según su ID
    permiso = get_object_or_404(Permiso, pk=permiso_id)
    permiso.delete()  # Eliminar el rol de la base de datos
    # Redirigir a la lista de roles después de eliminar
    return redirect('listar_permisos')


# CRUD ROL PERMISOS


def listar_rolpermisos(request):
    rolpermisos = RolPermiso.objects.select_related('rol', 'permiso').order_by('rol', 'permiso')
    headers =["Rol","Permisos"]

    return render(request, 'listar_rp.html', {'rolpermisos':rolpermisos, 'headers':headers})
    # rolpermisos = RolPermiso.objects.all()
    # return render(request, 'listar_rp.html', {'rolpermisos': rolpermisos})


def crear_rolpermiso(request):
    if request.method == 'POST':
        form = RolPermisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_rolpermisos')
    else:
        form = RolPermisoForm()
    return render(request, 'crear_rp.html', {'form': form})


def ver_rolpermiso(request, rp_id):
    rolpermiso = get_object_or_404(RolPermiso, pk=rp_id)
    return render(request, 'ver_rp.html', {'rolpermiso': rolpermiso})


def actualizar_rolpermiso(request, rp_id):
    rolpermiso = get_object_or_404(RolPermiso, pk=rp_id)
    if request.method == 'POST':
        form = RolPermisoForm(request.POST, instance=rolpermiso)
        if form.is_valid():
            form.save()
            return redirect('listar_rolpermisos')
    else:
        form = RolPermisoForm(instance=rolpermiso)
    return render(request, 'actualizar_rp.html', {'form': form, 'rolpermiso': rolpermiso})


def eliminar_rolpermiso(request, rp_id):
    # Obtener el rol específico según su ID
    rolpermiso = get_object_or_404(RolPermiso, pk=rp_id)
    rolpermiso.delete()  # Eliminar el rol de la base de datos
    # Redirigir a la lista de roles después de eliminar
    return redirect('listar_rolpermisos')
