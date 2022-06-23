from django.views.generic import TemplateView

# Create your views here.
DASHBOARD_TEMPLATE_PATH = "journal/general_app/templates/dashboards/index.html"


class DashBoardTemplateView(TemplateView):
    template_name = DASHBOARD_TEMPLATE_PATH
    
    def get_context_data(self, **kwargs):
        context = super(DashBoardTemplateView, self).get_context_data(**kwargs)
        
        
        
        return context