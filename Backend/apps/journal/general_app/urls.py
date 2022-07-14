from django.urls import path
from apps.journal.general_app import views

app_name = "journal_general"

urlpatterns = [
    path(
        'calendario/',
        views.DashBoardTemplateView.as_view(),
        name='calendar',
    ),
    path(
        'usos/',
        views.DashBoardTemplateView.as_view(),
        name='usage',
    ),
    path(
        'componentes/',
        views.DashBoardTemplateView.as_view(),
        name='components',
    ),
    path(
        'registro-de-cambios/',
        views.DashBoardTemplateView.as_view(),
        name='changelog',
    ),
    path(
        'editar-usuario/<pk>/',
        views.ManagementPeopleEditFormView.as_view(),
        name='edit-user',
    ),
    path(
        'editar-avatar/<pk>/',
        views.ManagementPeopleAvatarFormView.as_view(),
        name='edit-avatar',
    ),
]
