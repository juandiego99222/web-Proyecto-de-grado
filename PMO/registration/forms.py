from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):#mostrar el campo email en el formulario de registro
    email = forms.EmailField(required=True) 
    class Meta:
       model =User
       fields =("username","email","password1","password2")

    def clean_email(self): #funcion para que el email sea unico
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya está registrado, prueba con otro.")
        return email

class ProfileForm(forms.ModelForm):#formulario para perfil
    class Meta:
        model= Profile
        fields=['foto','profesion','telefono']
        widgets={
            'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'profesion':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Profesión u oficio'}),
            'telefono':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Telefono'}),
        }

class EmailForm(forms.ModelForm): #formulario para editar correo en perfil
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields=['email']

    def clean_email(self): #funcion para que el email sea unico
        email=self.cleaned_data.get("email")
        if 'email' in self.changed_data:
             if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El correo ya está registrado, prueba con otro.")
        return email