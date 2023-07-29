from django import forms
from django.core import validators
#paquete inicial basico de django para crear forms


class CursoFormulario(forms.Form):#nombre del formulario
    

    #defino los campos del formulario. Django viene con la logica de validacion de los valores
    nombre = forms.CharField(required=True, max_length=64, validators=[validators.RegexValidator(r'^[A-Za-z ]*$', 'Ingrese un nombre sin numeros.')])
    comision = forms.IntegerField(required=True, max_value=50000, widget=forms.NumberInput())
    profesor=forms.CharField(required=True, max_length=64)