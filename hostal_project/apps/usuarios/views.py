from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    headers = ['Nombre', 'Apellido', 'Correo', 'Rol', 'Activo']
    form = UsuarioForm()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios, 'headers': headers,'form':form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guardado con Éxito')
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return redirect('usuarios')

def eliminar_usuario(request,id):
    usuario = Usuario.objects.filter(pk=id)
    usuario.delete()
    messages.success(request,'Usuario Eliminado')
    return redirect('usuarios')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Actualizado')
            return redirect('usuarios')
        else:
            messages.error(request, 'Error al actualizar el usuario')
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'editar_usuario.html', {'form': form,'id':id})