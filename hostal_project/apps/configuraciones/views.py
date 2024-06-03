from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from .models import ConfiguracionGeneral
from .forms import ConfigForm

# Create your views here.
def listar_config(request):
    config= ConfiguracionGeneral.objects.all()
    headers=['Clave','Valor']
    form = ConfigForm()
    return render(request,'listar_config.html',{'form':form,'config':config,'headers':headers})

def crear_config(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guardado con Éxito')
            return redirect('listar_config')
    else:
        form = ConfigForm()      
    return render(request, 'listar_config.html', {'form': form})  

def eliminar_config(request,id):
    config = ConfiguracionGeneral.objects.filter(pk=id)
    config.delete()
    messages.success(request,'Eliminado con Éxtio')
    return redirect('listar_config')

def editar_config(request, id):
    config = get_object_or_404(ConfiguracionGeneral, pk=id)
    if request.method == 'POST':
        form = ConfigForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Actualizado')
            return redirect('listar_config')
        else:
            messages.error(request, 'Error al actualizar el usuario')
    else:
        form = ConfigForm(instance=config)
    return render(request, 'editar_config.html', {'form': form,'id':id})