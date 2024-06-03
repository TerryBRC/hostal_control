from django import forms
from .models import ConfiguracionGeneral

class ConfigForm(forms.ModelForm):
    class Meta:
        model= ConfiguracionGeneral
        fields= ['clave','valor']

        
