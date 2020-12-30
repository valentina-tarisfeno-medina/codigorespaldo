from django import forms
from .models import Sede, Detalle_dispo

class FormularioSede(forms.ModelForm):
    
    class Meta:
        model = Sede

        fields = ('nombre_sede','cantidad_estacionamiento')

        labels = {
            'nombre_sede':'Nombre Sede',
            'cantidad_estacionamiento':'cantidad_estacionamiento',

        }

        widgets = {
            'nombre_sede' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_estacionamiento' : forms.TextInput(attrs={'class':'form-control'})
             }

class FormularioDetalle_dispo(forms.ModelForm):
    
    class Meta:
        model = Detalle_dispo

        fields = ('sede','estado')

        labels = {
            'sede':'Sede',
            'estado':'Estado',
        }

        widgets = {
            'sede' : forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.TextInput(attrs={'class':'form-control'})
             }