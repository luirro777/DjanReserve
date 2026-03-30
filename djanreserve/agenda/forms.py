# agenda/forms.py
from django import forms
from .models import Agenda

class AgendaAdminForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['titulo','descripcion','persona', 'lugar', 'fecha', 'hora_comienzo', 'hora_final']
        widgets = {
            'hora_comienzo': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'hora_final': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
