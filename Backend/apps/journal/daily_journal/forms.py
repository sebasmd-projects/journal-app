from django import forms

from django.forms import ModelForm

from apps.authentication.users.models import PeopleModel
from apps.journal.daily_journal.models import JournalModel


class JournalForm(ModelForm):
    

    class Meta:
        model = JournalModel
        exclude = (
            'order',
            'updated',
            'created',
            'is_active'
        )
