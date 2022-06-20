from django.views.generic import TemplateView
from .models import LogoModel, StartDescriptionModel, ContentIndexModel

# Create your views here.
INDEX_PATH = 'home/templates/index.html'
DOCUMENTATION_PATH = "home/templates/documentation.html"


class IndexTemplateView(TemplateView):
    template_name = INDEX_PATH

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)

        context['start_description'] = StartDescriptionModel.objects.all()

        context['content_index'] = ContentIndexModel.objects.all()

        return context

class DocumentationTemplateView(TemplateView):
    template_name = DOCUMENTATION_PATH