from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import CourseTopicsModel, CoursesModel, GroupsModel


@admin.register(CourseTopicsModel)
class CourseTopicsModelAdmin(ImportExportActionModelAdmin, SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'id', 
        'course_topic_name',
        'is_active', 
        'created', 
        'updated'
    )

    list_display_links = ('id', 'course_topic_name')

    fieldsets = (
        ("Tema del curso", {
            "fields": (
                "course_topic_name",
                "course_topic_description"
            )
        }),
        ("Datos de visualización", {
            "fields": (
                "viewed_topic",
                "view_date_topic",
            )
        }),
        ("Otros datos", {
            "fields": (
                "id",
                "is_active",
                "created",
                "updated",
            )
        })
    )

    readonly_fields = (
        "id",
        "created",
        "updated",
    )
