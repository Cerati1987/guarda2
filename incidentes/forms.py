from django import forms
from core.models import Incidente

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ['descripcion', 'categoria', 'ubicacion', 'archivos']
