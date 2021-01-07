from sede.models import Sede
from django import forms
from .models import Registro, TipoRegistro

class FormularioRegistro(forms.ModelForm):
    
    class Meta:
        model = Registro

        fields = ('nombre','rut', 'patente','sede','usuario','tipo','motivo')

        labels = {
            'nombre':'Nombre',
            'rut':'Rut', 
            'patente':'Patente', 
            'sede':'Sede',
            'usuario':'Usuario',
            'tipo':'Tipo',
            'motivo':'Motivo'
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'rut' : forms.TextInput(attrs={'class':'form-control'}), 
            'patente' : forms.TextInput(attrs={'class':'form-control'}),
            'sede' : forms.Select(choices={}, attrs={'class':'form-control'}), 
            'fecha_entrada' : forms.DateTimeInput(attrs={'type':'date'}), 
            'tipo' : forms.Select(attrs={'class':'form-control'}),
            'motivo' : forms.TextInput(attrs={'class':'form-control'})
             }

class Formulariotipo_registro(forms.ModelForm):
    
    class Meta:
        model = TipoRegistro

        fields = ('id','nombre_registro')

        labels = {
            'id':'id',
            'nombre_registro':'nombre_registro'
        }

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_registro' : forms.TextInput(attrs={'class':'form-control'})
             }