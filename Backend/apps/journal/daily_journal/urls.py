from django.urls import path
from . import views

app_name = "journal"

urlpatterns = [
    path(
        'dashboard/',
        views.JournalFormView.as_view(),
        name='journal',
    ),
]
