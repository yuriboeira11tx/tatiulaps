from django import forms
from django.contrib.auth.models import User
from cadastro_abrigos.models import Abrigo
from cadastro_incidente.models import Incidente

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class BaseForm(forms.Form):
    username = forms.CharField(max_length=100)
    nome = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        abstract = True

class CidadeForm(BaseForm):
    pass

class EspecialistaForm(BaseForm):
    pass

class ONGForm(BaseForm):
   pass

class AbrigoForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        exclude = ()
