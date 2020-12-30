from django import forms
from .models import Sede, Detalle_dispo

class FormularioSede(forms.ModelForm):
    
    class Meta:
        model = Sede

        fields = ('campus_macul','campus_providencia','casa_central','cantidad_estacionamiento')

        labels = {
            'campus_macul':'Campus Macul',
            'campus_providencia':'Campus Providencia',
            'casa_central':'Casa Central ', 
            'cantidad_estacionamiento':'cantidad_estacionamiento',

        }

        widgets = {
            'campus_macul' : forms.TextInput(attrs={'class':'form-control'}),
            'campus_providencia': forms.TextInput(attrs={'class':'form-control'}),
            'casa_central' : forms.TextInput(attrs={'class':'form-control'}),
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