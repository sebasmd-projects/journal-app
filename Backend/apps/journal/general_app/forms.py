from django import forms

from django.forms import Form, ModelForm

from apps.authentication.users.models import PeopleModel


class ManagementPeopleEditForm(Form):
    MAN = 'M'
    WOMAN = 'W'
    OTHER = 'O'

    GENDER_IN_CHOICES = [
        ('','----'),
        (MAN, 'Hombre'),
        (WOMAN, 'Mujer'),
        (OTHER, 'Otro')
    ]

    first_name = forms.CharField(
        label='Nombres',
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "Cuáles son tus nombres?",
                "class": "form-control",
                "id": "management_people_edit_id_first_name",
            }
        )
    )

    last_name = forms.CharField(
        label='Apellidos',
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "Cuáles son tus apellidos?",
                "class": "form-control",
                "id": "management_people_edit_id_last_name",
            }
        )
    )

    phone = forms.CharField(
        label='Celular o teléfono',
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "Ingresa tu número de celular o teléfono",
                "class": "form-control",
                "id": "management_people_edit_id_phone",
            }
        )
    )

    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "placeholder": "Ingresa tu correo electrónico",
                "class": "form-control",
                "id": "management_people_edit_id_email",
            }
        )
    )

    birthday = forms.DateField(
        label='Fecha de nacimiento',
        required=True,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "placeholder": "Ingresa tu fecha de nacimiento",
                "class": "form-control",
                "id": "management_people_edit_id_birthday",
            }
        )
    )

    gender = forms.CharField(
        label='¿Con cuál genero te identificas?',
        required=True,
        widget=forms.Select(
            choices=GENDER_IN_CHOICES,
            attrs={
                "type": "text",
                "placeholder": "Ingresa tu genero",
                "class": "form-control",
                "id": "management_people_edit_id_gender"
            }
        )
    )


class ManagementPeopleAvatarForm(ModelForm):
    avatar = forms.ImageField(
        label='Avatar',
        required=False,
        widget=forms.FileInput(
            attrs={
                "type": "file",
                "placeholder": "Ingresa una foto de perfil",
                "class": "form-control",
                "id": "management_people_edit_id_avatar",
            }
        )
    )

    class Meta:
        model = PeopleModel
        fields = (
            'avatar',
        )
