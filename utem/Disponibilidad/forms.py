from django import forms
from .models import SedeCentro, SedeMacul, SedeProvidencia

class FormularioSedeCentro(forms.ModelForm):
    
    class Meta:
        model = SedeCentro

        fields = ('Sede','Tipousuario','Cantidad_estacionamientos')

        labels = {
            'Sede':'Sede',
            'Tipousuario':'Tipousuario',
            'Cantidad_estacionamientos':'Cantidad estacionamientos ', 

        }

        widgets = {
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Tipousuario': forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad_estacionamientos' : forms.TextInput(attrs={'class':'form-control'})
             }

class FormularioSedeMacul(forms.ModelForm):
    
    class Meta:
        model = SedeMacul

        fields = ('Sede','Tipousuario','Cantidad_estacionamientos')

        labels = {
            'Sede':'Sede',
            'Tipousuario':'Tipousuario',
            'Cantidad_estacionamientos':'Cantidad estacionamientos ', 

        }

        widgets = {
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Tipousuario': forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad_estacionamientos' : forms.TextInput(attrs={'class':'form-control'})
             }




class FormularioSedeProvidencia(forms.ModelForm):
    
    class Meta:
        model = SedeProvidencia

        fields = ('Sede','Tipousuario','Cantidad_estacionamientos')

        labels = {
            'Sede':'Sede',
            'Tipousuario':'Tipousuario',
            'Cantidad_estacionamientos':'Cantidad estacionamientos ', 

        }

        widgets = {
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Tipousuario': forms.TextInput(attrs={'class':'form-control'}),
            'Cantidad_estacionamientos' : forms.TextInput(attrs={'class':'form-control'})
             }