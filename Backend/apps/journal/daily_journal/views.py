from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from apps.journal.daily_journal.forms import JournalForm



JOURNAL_TEMPLATE_PATH = "journal/daily_journal/templates/dashboards/journal.html"

class JournalFormView(FormView):
    template_name = JOURNAL_TEMPLATE_PATH
    form_class = JournalForm
    success_url = '/'
