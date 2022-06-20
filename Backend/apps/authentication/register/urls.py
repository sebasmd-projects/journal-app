from django.urls import path
from . import views

app_name = "authentication_register"

urlpatterns = [
    path(
        'auth/registro/', 
        views.UserRegisterView.as_view(), 
        name='user-register',
    ),
    path(
        'auth/verificar-usuario/<pk>/', 
        views.VerificationCodeView.as_view(), 
        name='user-verification',
    ),
]