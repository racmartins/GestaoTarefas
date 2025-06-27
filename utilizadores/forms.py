from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistoForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Nome de utilizador",
            "email": "E-mail",
            "password1": "Palavra-passe",
            "password2": "Confirmar palavra-passe",
        }
