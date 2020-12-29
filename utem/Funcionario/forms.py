from django import forms
from .models import Registro

class FormularioRegistro(forms.ModelForm):
    
    class Meta:
        model = Registro

        fields = ('nombre','rut', 'patente', 'sede','fecha_salida','tipo','motivo')

        labels = {
            'Nombre':'Nombre',
            'Rut':'Rut', 
            'Patente':'Patente', 
            'usuario':'usuario',
            'Sede':'Sede',
            'matriz':'matriz',
            'fecha_salida':'fecha_salida',
            'tipo':'tipo',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'usuario': forms.TextInput(attrs={'class':'form-control'}),
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'matriz' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Ingreso' : forms.DateInput(attrs={'type':'date'}), 
            'fecha_salida' : forms.DateInput(attrs={'type':'date'})
             }





        


