from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, label='Ingrese su nombre')
    apellido = forms.CharField(max_length=30, label='Ingrese su apellido')
    email = forms.EmailField()

class MiTarea(forms.Form):
    titulo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=100)
    completada= forms.BooleanField(initial=False, required=False)

class MiNota(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=100)

