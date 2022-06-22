from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path(
        '', 
        views.IndexTemplateView.as_view(), 
        name='inicio',
    ),
    path(
        'documentation', 
        views.DocumentationTemplateView.as_view(), 
        name='documentation',
    ),
    path(
        'ver-requests',
        views.SeeRequestsView.as_view(),
        name='ver-requests',
    )
]