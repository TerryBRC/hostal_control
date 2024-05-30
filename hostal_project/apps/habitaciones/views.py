from django.shortcuts import render, get_object_or_404, redirect
from .models import Habitacion, TipoHabitacion
from .forms import HabitacionForm, TipoHabitacionForm

# Vistas para Habitacion


def listar_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'listar_habitaciones.html', {'habitaciones': habitaciones})


def crear_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_habitaciones')
    else:
        form = HabitacionForm()
    return render(request, 'crear_habitacion.html', {'form': form})


def ver_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    return render(request, 'ver_habitacion.html', {'habitacion': habitacion})


def editar_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('listar_habitaciones')
    else:
        form = HabitacionForm(instance=habitacion)
    return render(request, 'editar_habitacion.html', {'form': form})


def eliminar_habitacion(request, pk):
    habitacion = get_object_or_404(Habitacion, pk=pk)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('listar_habitaciones')

# Vistas para TipoHabitacion


def listar_tipo_habitaciones(request):
    tipo_habitaciones = TipoHabitacion.objects.all()
    return render(request, 'listar_tipo_habitaciones.html', {'tipo_habitaciones': tipo_habitaciones})


def crear_tipo_habitacion(request):
    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_habitaciones')
    else:
        form = TipoHabitacionForm()
    return render(request, 'crear_tipo_habitacion.html', {'form': form})


def ver_tipo_habitacion(request, pk):
    tipo_habitacion = get_object_or_404(TipoHabitacion, pk=pk)
    return render(request, 'ver_tipo_habitacion.html', {'tipo_habitacion': tipo_habitacion})


def editar_tipo_habitacion(request, pk):
    tipo_habitacion = get_object_or_404(TipoHabitacion, pk=pk)
    if request.method == 'POST':
        form = TipoHabitacionForm(request.POST, instance=tipo_habitacion)
        if form.is_valid():
            form.save()
            return redirect('listar_tipo_habitaciones')
    else:
        form = TipoHabitacionForm(instance=tipo_habitacion)
    return render(request, 'editar_tipo_habitacion.html', {'form': form})


def eliminar_tipo_habitacion(request, pk):
    tipo_habitacion = get_object_or_404(TipoHabitacion, pk=pk)
    if request.method == 'POST':
        tipo_habitacion.delete()
        return redirect('listar_tipo_habitaciones')
