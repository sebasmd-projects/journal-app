from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

from apps.authentication.users.managers import UsersManager

from apps.journal.groups.models import GroupsModel


class PeopleModel(models.Model):
    TEACHER = 'T'
    MANAGER = 'M'
    SUPERUSER = 'S'
    EDITOR = 'E'
    ASSISTANT = 'A'

    MAN = 'M'
    WOMAN = 'W'
    OTHER = 'O'

    ROLE_IN_CHOICES = [
        (TEACHER, 'Profesor'),
        (MANAGER, 'Administrador'),
        (SUPERUSER, 'Superusuario'),
        (EDITOR, 'Editor'),
        (ASSISTANT, 'Asistente'),
    ]

    GENDER_IN_CHOICES = [
        (MAN, 'Hombre'),
        (WOMAN, 'Mujer'),
        (OTHER, 'Otro')
    ]

    first_name = models.CharField(
        'Nombres',
        max_length=40,
        help_text="Nombres del usuario",
        default='',
    )

    last_name = models.CharField(
        'Apellidos',
        max_length=40,
        help_text="Apellidos del usuario",
        default='',
    )

    full_name = models.CharField(
        'Nombres y Apellidos',
        max_length=100,
        help_text="Nombres y apellidos del usuario",
        default='',

    )

    avatar = models.ImageField(
        blank=True,
        null=True,
        default='users/default.jpg'
    )

    phone = models.CharField(
        "Celular o teléfono",
        max_length=20,
        help_text="Celular o teléfono del usuario",
        default='',
    )

    groups = models.ManyToManyField(
        GroupsModel,
        verbose_name="Grupos del usuario",
        blank=True,
    )

    role = models.CharField(
        "Rol",
        max_length=1,
        choices=ROLE_IN_CHOICES,
        default=TEACHER,
        help_text="Rol del usuario"
    )

    birthday = models.DateField(
        "Fecha de nacimiento",
        help_text="Fecha de nacimiento del usuario",
        default=timezone.now,
        blank=True,
        null=True
    )

    age = models.CharField(
        "Edad",
        default=0,
        max_length=4,
        help_text="Edad del usuario",
    )

    gender = models.CharField(
        "Género",
        choices=GENDER_IN_CHOICES,
        max_length=1,
        default=OTHER,
    )

    is_active = models.BooleanField(
        'Es una persona activa',
        default=True,
        help_text="Designa si la persona está activa"
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación del usuario",
        blank=True, null=True
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición del usuario",
        blank=True, null=True
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    def save(self, *args, **kwargs):
        
        self.full_name = f"{self.first_name} {self.last_name}"

        self.age = date.today().year - self.birthday.year - (
            (
                date.today().month, date.today().day
            ) < (
                self.birthday.month, self.birthday.day
            )
        )
        
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'apps_authentication_people'
        ordering = ['order']

    def __str__(self) -> str:
        return f"{self.id} - {self.first_name} {self.last_name} - {self.role}"


class UsersModel(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        "Usuario",
        max_length=150,
        unique=True,
        help_text="Requerido. 150 carácteres o menos. Alfanumérico y @.+-_ only.",
        validators=[username_validator],
        error_messages={
            "único": "Un usuario con este nombre de usuario ya existe",
        },
    )

    email = models.EmailField(
        'Correo',
        max_length=254,
        unique=True,
        help_text="Requerido. 254 carácteres o menos. Formato de correo válido.",
        error_messages={
            "único": "Este correo ya existe",
        }
    )

    people = models.OneToOneField(
        PeopleModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    privacy = models.BooleanField(
        'Términos y Condiciones',
        default=False,
        help_text="Requerido. Acepta los términos y condiciones.",
        error_messages={
            "requerido": "Debe aceptar los términos y condiciones",
        }
    )

    verification_code = models.CharField(
        'Código de verificación',
        max_length=4,
        default='0000',
        help_text="Requerido. 4 carácteres o menos. Generado automáticamente y llega al correo",
        error_messages={
            "requerido": "Debe ingresar el código de verificación",
        }
    )

    is_staff = models.BooleanField(
        "Es un administrador",
        default=False,
        help_text="Designa si el usuario puede acceder al administrador",
    )

    is_active = models.BooleanField(
        'Es un usuario activo',
        default=False,
        help_text="Designa si el usuario está activo",
    )

    date_joined = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación del usuario",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición del usuario",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UsersManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        unique_together = ('username', 'email')
        db_table = 'apps_authentication_users'
        ordering = ['order']

    def __str__(self) -> str:
        return f"{self.id} - {self.username} - {self.email}"
