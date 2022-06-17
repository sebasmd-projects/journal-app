from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class UsersModel(AbstractBaseUser):
    """Modelo de usuario

    Args:
        AbstractBaseUser (class): Herencia del modelo de usuario de Django
    """

    username = models.CharField(
        'Nombre de usuario', max_length=40, unique=True)
    email = models.EmailField('Correo', max_length=254, unique=True)
    names = models.CharField('Nombres', max_length=40)
    surnames = models.CharField('Apellidos', max_length=40)
    privacy = models.BooleanField('Términos y Condiciones', default=False)
    verification_code = models.CharField(
        'Código de verificación', max_length=4, default='0000'
    )

    created = models.DateTimeField('Fecha de cración', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)
    order = models.PositiveIntegerField('Orden')

    def get_short_name(self) -> str:
        return self.username

    def get_full_name(self) -> str:
        return f"{self.names} {self.surnames}"

    def __str__(self) -> str:
        return f"{self.id} - {self.username} - {self.email}"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        unique_together = ('username', 'email')
        db_table = 'apps_auth_users'
        ordering = ['order']
