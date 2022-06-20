from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import LogoModel, StartDescriptionModel, ContentIndexModel

@admin.register(LogoModel)
class LogoAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (
            "Logo modo luz",{
                "fields":(
                    "logo_light",
                )
            },   
        ),
        (
            "Logo modo oscuro",{
                "fields":(
                    "logo_dark",
                )
            },
        ),
        (
            "Favicon",{
                "fields":(
                    "favicon",
                )
            }
        ),
        (
            "Otros datos",{
                "fields":(
                    "is_active",
                    "created",
                    "updated",
                )
            }
        ),
    )
    
    readonly_fields = (
        "created",
        "updated",
    )
    
    list_display = (
        "order",
        "title",
        "id",
        "created",
        "updated",
    )
    
    list_display_links = (
        "title",
        "id",
        "created",
        "updated",
    )

@admin.register(StartDescriptionModel)
class StartDescriptionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "order",
        "id",
        "is_active",
        "created",
        "updated",
    )
    
    list_display_links = (
        "id",
        "is_active",
        "created",
        "updated",
    )
    
@admin.register(ContentIndexModel)
class ContentIndexAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        "order",
        "id",
        "is_active",
        "created",
        "updated",
    )
    
    list_display_links = (
        "id",
        "is_active",
        "created",
        "updated",
    )