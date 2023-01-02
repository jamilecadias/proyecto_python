from django import forms
from AppCoder.models import *

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    numero_dia=forms.IntegerField()