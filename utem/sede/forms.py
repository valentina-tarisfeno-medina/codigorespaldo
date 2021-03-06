
from sede.models import Sede
from django import forms


class FormularioSede(forms.ModelForm):
    
    class Meta:
        model = Sede

        fields = ('nombre_sede','cantidad_estacionamiento')

        labels = {
            'nombre_sede':'Nombre Sede',
            'cantidad_estacionamiento':'Cantidad Estacionamiento',

        }

        widgets = {
            'nombre_sede' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_estacionamiento' : forms.TextInput(attrs={'class':'form-control'})
             }