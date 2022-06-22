from django.urls import path
from . import views

app_name = "authentication_register"

urlpatterns = [
    path(
        'registro/', 
        views.UserRegisterView.as_view(), 
        name='user-register',
    ),
    path(
        'verificar-usuario/<pk>/', 
        views.VerificationCodeView.as_view(), 
        name='user-verification',
    ),
]