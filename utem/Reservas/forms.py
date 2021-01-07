from sede.models import Sede
from django import forms
from .models import Reserva

class FormularioReserva(forms.ModelForm):
    
    class Meta:
        model = Reserva

        fields = ('nombre_reserva','rut_reserva','usuario_reserva','fecha_reserva','cantidad_horas','patente','sede','motivo')


        labels = {
            'nombre_reserva':'Nombre reserva',
            'rut_reserva':'Rut reserva', 
            'usuario_reserva':'Usuario Reserva ', 
            'fecha_reserva':'Fecha Reserva',
            'cantidad_horas':'Cantidad horas ', 
            'patente':'Patente', 
            'sede':'Sede',
            'motivo':'Motivo'
        }

        widgets = {
            'nombre_reserva' : forms.TextInput(attrs={'class':'form-control'}),
            'rut_reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'usuario_reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'cantidad_horas' : forms.TextInput(attrs={'class':'form-control'}), 
            'fecha_reserva' : forms.DateTimeInput(attrs={'type':'date'}),
            'patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'sede' : forms.Select(choices={}, attrs={'class':'form-control'}), 
            'motivo' : forms.TextInput(attrs={'class':'form-control'})
             }


