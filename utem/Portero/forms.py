from django import forms
from .models import Portero, Porteromacul, Porteroprovidencia

class FormularioPortero(forms.ModelForm):
    
    class Meta:
        model = Portero
        fields = ('Nombre','Rut','Sede','Fin_Turno')

        labels = {
                'Nombre':'Nombre',
                'Rut':'Rut', 
                'Sede':'Sede',
                'Incio_Turno':'Incio Turno',
                'Fin_Turno':'Fin Turno'
            }

        widgets = {
                'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
                'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
                'Sede' : forms.TextInput(attrs={'class':'form-control'}),
                'Incio_Turno' : forms.DateInput(attrs={'type':'date'}), 
                'Fin_Turno' : forms.DateInput(attrs={'type':'date'})
                }



class FormularioPorteromacul(forms.ModelForm):
    
    class Meta:
        model = Porteromacul
        fields = ('Nombre','Rut','Sede','Fin_Turno')

        labels = {
                'Nombre':'Nombre',
                'Rut':'Rut', 
                'Sede':'Sede',
                'Incio_Turno':'Incio Turno',
                'Fin_Turno':'Fin Turno'
            }

        widgets = {
                'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
                'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
                'Sede' : forms.TextInput(attrs={'class':'form-control'}),
                'Incio_Turno' : forms.DateInput(attrs={'type':'date'}), 
                'Fin_Turno' : forms.DateInput(attrs={'type':'date'})
                }



class FormularioPorteroprovidencia(forms.ModelForm):
    
    class Meta:
        model = Porteroprovidencia
        fields = ('Nombre','Rut','Sede','Fin_Turno')

        labels = {
                'Nombre':'Nombre',
                'Rut':'Rut', 
                'Sede':'Sede',
                'Incio_Turno':'Incio Turno',
                'Fin_Turno':'Fin Turno'
            }

        widgets = {
                'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
                'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
                'Sede' : forms.TextInput(attrs={'class':'form-control'}),
                'Incio_Turno' : forms.DateInput(attrs={'type':'date'}), 
                'Fin_Turno' : forms.DateInput(attrs={'type':'date'})
                }

