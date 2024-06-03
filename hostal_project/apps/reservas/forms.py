from django import forms
from .models import *

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente',
                  'habitacion',
                  'fecha_entrada',
                  'fecha_salida',
                  'numero_huespedes'
                  ,'estado_reserva']
    def __init__(self, *args, **kwargs):  # Definimos el método init para personalizar el formulario
        super().__init__(*args, **kwargs)  # Llamamos al init del formulario base para inicializarlo correctamente
        # Modificamos el queryset del campo 'habitacion' para que solo incluya las habitaciones disponibles
        self.fields['habitacion'].queryset = Habitacion.objects.filter(disponible=True)