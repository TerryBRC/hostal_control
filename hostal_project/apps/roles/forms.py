from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre_rol', 'descripcion']
        # Puedes agregar widgets personalizados u otras configuraciones aquí si es necesario
