from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import *
from .forms import *

def listar_reservas(request):
    reservas = Reserva.objects.all()
    headers=['cliente','Habitación','Entrada','Salida','Cantidad','Estado']
    form = ReservaForm()
    return render(request,'listar_reservas.html',{'form':form,'headers':headers,'reservas':reservas})

def crear_reserva(request):
    if request.method=='POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save
            messages.success(request,'Guardado con Éxito')
        else:
            messages.error(request,'Error al Guardar')
    else:
        form=ReservaForm()
    return redirect('listar_reservas')

def editar_reserva(request,id):
    reserva = get_object_or_404(Reserva,pk=id)
    if request.method =='POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado con Éxito")
            redirect('listar_reservas')
        else:
            messages.error(request,'Error al Actualizar')
    else:
        form=ReservaForm(instance=reserva)
    return render(request,'editar_reserva.html',{'form':form,'id':id})

def eliminar_reserva(request,id):
    reserva = Reserva.objects.filter(pk=id)
    reserva.delete()
    messages.success(request,'Eliminado con Éxito')
    return redirect('listar_reservas')