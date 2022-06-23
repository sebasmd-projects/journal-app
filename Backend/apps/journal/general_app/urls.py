from django.urls import path
from . import views

app_name = "journal_general"

urlpatterns = [
    path(
        'dashboard/', 
        views.DashBoardTemplateView.as_view(), 
        name='dashboard',
    ),
]