
from django import forms
from .models import Habitacion, TipoHabitacion


class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'


class TipoHabitacionForm(forms.ModelForm):
    class Meta:
        model = TipoHabitacion
        fields = ['tipo_habitacion', 'descripcion']
