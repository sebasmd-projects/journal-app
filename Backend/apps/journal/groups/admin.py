from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import CourseTopicsModel, CoursesModel, GroupsModel


@admin.register(CourseTopicsModel)
class CourseTopicsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'id',
        'course_topic_name',
        'is_active',
        'created',
        'updated'
    )

    list_display_links = (
        'id',
        'course_topic_name'
    )

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


@admin.register(CoursesModel)
class CoursesAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'course_name',
        'short_course_name',
        'is_active',
        'created',
        'updated'
    )

    list_display_links = (
        'course_name',
        'short_course_name',
    )

    fieldsets = (
        ("Curso", {
            "fields": (
                "course_name",
                "short_course_name",
                "course_description",
            )
        }),
        ("Temas", {
            "fields": (
                "topics",
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
    
    filter_horizontal = (
        'topics',
    )



@admin.register(GroupsModel)
class GroupsAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = (
        'group_name',
        'is_active',
        'created',
        'updated'
    )

    fieldsets = (
        ("Grupo", {
            "fields": (
                "group_name",
                "courses"
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
    
    filter_horizontal = (
        'courses',
    )

    