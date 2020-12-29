from django import forms
from .models import  Visitante, Visitantemacul, Visitanteprovidencia

class FormularioVisitante(forms.ModelForm):
    
    class Meta:
        model = Visitante
        fields = ('Nombre','Rut', 'Patente', 'Sede','Fecha_Salida','Motivo')
        
        labels = {
            'Nombre':'Nombre',
            'Rut':'Rut', 
            'Patente':'Patente', 
            'Sede':'Sede',
            'Fecha_Salida':'Fecha_Salida',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Ingreso' : forms.DateInput(attrs={'type':'date'}), 
            'Fecha_Salida' : forms.DateInput(attrs={'type':'date'})
             }

class FormularioVisitantemacul(forms.ModelForm):
    
    class Meta:
        model = Visitantemacul
        fields = ('Nombre','Rut', 'Patente', 'Sede','Fecha_Salida','Motivo')
        
        labels = {
            'Nombre':'Nombre',
            'Rut':'Rut', 
            'Patente':'Patente', 
            'Sede':'Sede',
            'Fecha_Salida':'Fecha_Salida',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Ingreso' : forms.DateInput(attrs={'type':'date'}), 
            'Fecha_Salida' : forms.DateInput(attrs={'type':'date'})
             }

class FormularioVisitanteprovidencia(forms.ModelForm):
    
    class Meta:
        model = Visitanteprovidencia
        fields = ('Nombre','Rut', 'Patente', 'Sede','Fecha_Salida','Motivo')
        
        labels = {
            'Nombre':'Nombre',
            'Rut':'Rut', 
            'Patente':'Patente', 
            'Sede':'Sede',
            'Fecha_Salida':'Fecha_Salida',
            'Motivo':'Motivo'
        }

        widgets = {
            'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'Rut' : forms.TextInput(attrs={'class':'form-control'}), 
            'Patente' : forms.TextInput(attrs={'class':'form-control'}), 
            'Sede' : forms.TextInput(attrs={'class':'form-control'}),
            'Motivo' : forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Ingreso' : forms.DateInput(attrs={'type':'date'}), 
            'Fecha_Salida' : forms.DateInput(attrs={'type':'date'})
             }