from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Cliente
from .forms import ClienteForm
# Create your views here.
def listar_clientes(request):
    clientes = Cliente.objects.all()
    headers = ['Nombre','Apellido','Dirección','Teléfono','E-mail']
    form = ClienteForm()
    return render(request,'listar_clientes.html',{'form':form,'clientes':clientes,'headers':headers})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Guardado con Éxito')
            return redirect('listar_clientes')
    else:
        form=ClienteForm()
    return redirect('listar_clientes')

def editar_cliente(request,id):
    cliente= get_object_or_404(Cliente,pk=id)
    if request.method =='POST':
        form = ClienteForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request,'Actualizado con Éxito')
            return redirect('listar_clientes')
        else:
            messages.error(request,'Error al actualizar')
    else:
        form=ClienteForm(instance=cliente)
    return render(request,'editar_cliente.html',{'form':form,'id':id})


def eliminar_cliente(request,id):
    cliente = Cliente.objects.filter(pk=id)
    cliente.delete()
    messages.success(request,'Eliminado con Éxito')
    return redirect('listar_clientes')