from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class UsersManager(BaseUserManager, models.Manager):

    # Función privada para crear usuario
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError("Ingresa un usuario")
        email = self.normalize_email(email)
        # La variable user llama al modelo asociado a este manager usando el self.model
        # se le pasan todos los valores obligatorios para crear un usuario
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        # La contraseña debe estar encriptada por tanto no se coloca dentro del modelo
        # se le pasa la contraseña a set_password para que la encripte
        user.password = make_password(password)

        # Se guarda el usuario
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None,  **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(username, email, password, **extra_fields)

    def cod_validation(self, user_id, register_cod):
        if self.filter(id=user_id, verification_code=register_cod).exists():
            return True
        else:
            return False
