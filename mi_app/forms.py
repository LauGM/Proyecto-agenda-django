from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, label='Ingrese su nombre')
    apellido = forms.CharField(max_length=30, label='Ingrese su apellido')
    email = forms.EmailField()