from django import forms
from django.contrib.auth import authenticate
from .functions import password_validation
from ..users.models import UsersModel


class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Usuario',
                'class': 'form-control',
                'id': 'register_id_username'
            }
        )
    )

    email = forms.CharField(
        label='Correo',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'placeholder': 'Correo',
                'class': 'form-control',
                'id': 'register_id_email'
            }
        )
    )

    privacy = forms.BooleanField(
        label='Términos y Condiciones',
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'type': 'checkbox',
                'id': 'register_id_privacy'
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
                'id': 'register_id_password'
            }
        )
    )

    repeat_password = forms.CharField(
        label='Repetir contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'placeholder': 'Repetir contraseña',
                'class': 'form-control',
                'id': 'register_id_repeat_password'
            }
        )
    )

    class Meta:
        model = UsersModel
        fields = (
            'username',
            'email',
            'privacy',
        )

    def clean_repeat_password(self):
        password_validation(
            self, self.cleaned_data['password'], self.cleaned_data['repeat_password'])


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(
        label='Código de verificación',
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'placeholder': 'Código de verificación',
                'class': 'form-control',
                'id': 'verfication_code_id'
            }
        )
    )

    def __init__(self, pk, *args, **kwargs):
        self.user_id = pk
        super(VerificationCodeForm, self).__init__(*args, **kwargs)

    def clean_verificationcode(self):
        cod = self.cleaned_data['verification_code']

        if len(cod) == 4:
            active = UsersModel.objects.cod_validation(
                self.user_id['pk'],
                cod
            )
            if not active:
                raise forms.ValidationError(
                    'El código ingresado no es correcto')
        else:
            raise forms.ValidationError('El código ingresado no es correcto')
