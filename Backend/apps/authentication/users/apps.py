from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.authentication.users'
    verbose_name: str = 'Autentificación'
    verbose_name_plural: str = 'Autentificación'