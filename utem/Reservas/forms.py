from django import forms
from .models import Reserva, Reservamacul, Reservaprovidencia

class FormularioReserva(forms.ModelForm):
    
    class Meta:
        model = Reserva

        fields = ('Nombre_reserva','Rut_reserva','Usuario_Reserva','Fecha_Reserva','Cantidad_horas','Patente','Sede','Motivo')


        labels = {
            'Nombre_reserva':'Nombre reserva',
            'Rut_reserva':'Rut reserva', 
            'Usuario_Reserva':'Usuario Reserva ', 
            'Fecha_Reserva':'Fecha_Reserva',
            'Cantidad_horas':'Cantidad horas ', 
            'Patente':'Patente', 
            'Sede':'Sede',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre_reserva' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut_reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'Usuario_Reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'Cantidad_horas' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Reserva' : forms.DateInput(attrs={'type':'date'})
             }


class FormularioReservamacul(forms.ModelForm):
    
    class Meta:
        model = Reservamacul

        fields = ('Nombre_reserva','Rut_reserva','Usuario_Reserva','Fecha_Reserva','Cantidad_horas','Patente','Sede','Motivo')


        labels = {
            'Nombre_reserva':'Nombre reserva',
            'Rut_reserva':'Rut reserva', 
            'Usuario_Reserva':'Usuario Reserva ', 
            'Fecha_Reserva':'Fecha_Reserva',
            'Cantidad_horas':'Cantidad horas ', 
            'Patente':'Patente', 
            'Sede':'Sede',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre_reserva' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut_reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'Usuario_Reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'Cantidad_horas' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Reserva' : forms.DateInput(attrs={'type':'date'})
             }



class FormularioReservaprovidencia(forms.ModelForm):
    
    class Meta:
        model = Reservaprovidencia

        fields = ('Nombre_reserva','Rut_reserva','Usuario_Reserva','Fecha_Reserva','Cantidad_horas','Patente','Sede','Motivo')


        labels = {
            'Nombre_reserva':'Nombre reserva',
            'Rut_reserva':'Rut reserva', 
            'Usuario_Reserva':'Usuario Reserva ', 
            'Fecha_Reserva':'Fecha_Reserva',
            'Cantidad_horas':'Cantidad horas ', 
            'Patente':'Patente', 
            'Sede':'Sede',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre_reserva' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut_reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'Usuario_Reserva' : forms.TextInput(attrs={'class':'form-control'}), 
            'Cantidad_horas' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Reserva' : forms.DateInput(attrs={'type':'date'})
             }