from django import forms
from django.forms import ValidationError, DateField, EmailField, CharField, Form, ImageField, PasswordInput, SlugField
from .models import Receta, Tamaño, Caracteristica, Funcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Error1',
                            params={'valor':value})


class ContactoForm(forms.Form):

    nombre = forms.CharField(
            label='Nombre',
            required=True,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            error_messages={
                    'required': 'Por favor completa el campo',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Ingrese su email'})
            )
    telefono = forms.CharField(
            label='Telefono',
            max_length=12,
            widget= forms.TextInput(attrs={'class':'form-control','type':'tel','placeholder':'Enter your phone number...'})
            )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':7,'type':'textarea','placeholder':'Enter your messages...'})
            )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("El mensaje no puede ser menor a 10 caracteres")
        return data


class RecetaForm(forms.ModelForm):
    nombre = forms.CharField(error_messages={'required': 'dale, inventate un nombre al menos'})
    
    class Meta:
        model = Receta
        fields = '__all__'    
        widgets = {
            'Ingredientes': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
            'preparacion': forms.Textarea(attrs={'cols': 20, 'rows': 20}),
        }
    
class RecetaFormValidado(RecetaForm):
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre.upper() == "AGUA":
            raise ValidationError("El Agua no es un trago, es solo agua")

        return nombre
    

class TamañoForm(forms.ModelForm):
    nombre = forms.CharField(error_messages={'required': 'dale, inventate un nombre al menos'})
    
    class Meta:
        model = Tamaño
        fields = '__all__'
    
class FuncionForm(forms.ModelForm):
    nombre = forms.CharField(error_messages={'required': 'dale, inventate un nombre al menos'})
    
    class Meta:
        model = Funcion
        fields = '__all__'

class CaracteristicaForm(forms.ModelForm):
    nombre = forms.CharField(error_messages={'required': 'dale, inventate un nombre al menos'})
    
    class Meta:
        model = Caracteristica
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = CharField(label='Nombre/s', widget=forms.TextInput)
    last_name = CharField(label='Apellido/s', widget=forms.TextInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_text = {k:"" for k in fields}

