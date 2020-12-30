from django import forms
from .models import Registro, tipo_registro

class FormularioRegistro(forms.ModelForm):
    
    class Meta:
        model = Registro

        fields = ('nombre','rut', 'patente','sede','usuario','fecha_salida','tipo','motivo')

        labels = {
            'nombre':'nombre',
            'rut':'rut', 
            'patente':'patente', 
            'sede':'sede',
            'usuario':'usuario',
            'fecha_salida':'fecha_salida',
            'tipo':'tipo',
            'motivo':'motivo'
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'rut' : forms.TextInput(attrs={'class':'form-control'}), 
            'patente' : forms.TextInput(attrs={'class':'form-control'}),
            'sede' : forms.TextInput(attrs={'class':'form-control'}), 
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_entrada' : forms.DateInput(attrs={'type':'date'}), 
            'fecha_salida' : forms.DateInput(attrs={'type':'date'}),
            'tipo' : forms.TextInput(attrs={'class':'form-control'}),
            'motivo' : forms.TextInput(attrs={'class':'form-control'})
             }


class Formulariotipo_registro(forms.ModelForm):
    
    class Meta:
        model = tipo_registro

        fields = ('nombre')

        labels = {
            'nombre':'nombre'
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'})
             }