from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Files


class FileForm(forms.ModelForm):#formulario para perfil
    class Meta:
        model= Files
        fields=['title','upload']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Archivo'}),
            
        }