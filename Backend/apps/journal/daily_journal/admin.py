from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from .models import JournalModel

class JournalResources(resources.ModelResource):
    class Meta:
        model = JournalModel
        fields = (
            "order",
            "teacher",
            "group",
            "course",
            "topic",
            "journal_date",
            "pedagogical_reflection",
            "observations",
            "description",
            "created",
            "updated",
        )
        
        
@admin.register(JournalModel)
class JournalAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    resource_class = JournalResources
    
    list_display = (
        "id",
        "teacher",
        "group",
        "course",
        "topic",
        "journal_date",
    )
    
    list_display_links = (
        "id",
        "teacher",
        "group",
    )