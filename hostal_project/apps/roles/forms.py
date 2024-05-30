from django import forms
from .models import Rol, Permiso


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre_rol', 'descripcion']
        # Puedes agregar widgets personalizados u otras configuraciones aquí si es necesario


class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['nombre_permiso','descripcion']
