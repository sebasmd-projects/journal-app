from django import forms
from django.contrib.auth import authenticate
from ..register.functions import password_validation
from . import models


class UserLoginForm (forms.Form):
    username = forms.CharField(
        label='Correo',
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Usuario',
                'class': 'form-control',
                'id': 'login_id_username'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Contraseña',
                'class': 'form-control',
                'id': 'login_id_password'
            }
        )
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                'Los datos de acceso no son correctos'
            )

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label='Contraseña Actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Contraseña Actual',
                'class': 'form-control',
                'id': 'actual_id_password'
            }
        )
    )

    new_password = forms.CharField(
        label='Contraseña Nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Contraseña Nueva',
                'class': 'form-control',
                'id': 'new_id_password'
            }
        )
    )

    confirm_password = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Confirmar Contraseña',
                'class': 'form-control',
                'id': 'confirm_id_password'
            }
        )
    )

    def clean_repeat_password(self):
        password_validation(
            self, self.cleaned_data['new_password'], self.cleaned_data['confirm_password']
        )
