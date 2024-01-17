from tkinter import Widget
from django import forms
from django.db import models
from .models import *

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:20px;'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:20px;'}))
    rut = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'style':'margin-bottom:20px;'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:20px;'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'style':'margin-bottom:20px;'}))
    telefono = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'style':'margin-bottom:20px;'}))

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = ""
        self.fields['apellido'].label = ""
        self.fields['rut'].label = ""
        self.fields['direccion'].label = ""
        self.fields['correo'].label = ""
        self.fields['telefono'].label = ""