from django import forms
from .models import Portero

class FormularioPortero(forms.ModelForm):
    
    class Meta:
        model = Portero
        fields = ('nombre','rut','sede','fin_Turno')

        labels = {
                'nombre':'Nombre',
                'rut':'Rut', 
                'sede':'Sede',
                'incio_Turno':'Incio Turno',
                'fin_Turno':'Fin Turno'
            }

        widgets = {
                'nombre' : forms.TextInput(attrs={'class':'form-control'}),
                'rut' : forms.TextInput(attrs={'class':'form-control'}), 
                'sede' : forms.TextInput(attrs={'class':'form-control'}),  
                'incio_Turno' : forms.DateInput(attrs={'type':'date'}), 
                'fin_Turno' : forms.DateInput(attrs={'type':'date'})
                }