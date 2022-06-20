from django.urls import path
from . import views

app_name = "authentication_login"

urlpatterns = [
    path(
        'auth/iniciar-sesion/', 
        views.UserLoginView.as_view(), 
        name='user-login',
    ),
    path(
        'auth/cerrar-sesion/', 
        views.UserLogoutView.as_view(), 
        name='user-logout',
    ),
    path(
        'auth/cambiar-contraseña/', 
        views.UpdatePassword.as_view(), 
        name='user-update-password',
    ),
]