from django.db import models
from django.utils import timezone

# Create your models here.


class CourseTopicsModel(models.Model):
    course_topic_name = models.CharField(
        "Nombre del tema",
        max_length=100
    )

    course_topic_description = models.TextField(
        "Descripción del tema"
    )

    viewed_topic = models.BooleanField(
        "¿Ya se visualizó el tema?",
        default=False
    )

    view_date_topic = models.DateTimeField(
        "Fecha de visualización del tema",
    )

    is_active = models.BooleanField(
        'Es un tema activo',
        default=True,
        help_text="Designa si el tema está activo",
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación del tema",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición del tema",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'
        db_table = 'apps_journal_groups_coursetopics'
        ordering = ['order']

    def __str__(self):
        return self.course_topic_name


class CoursesModel(models.Model):
    course_name = models.CharField(
        "Nombre del curso",
        max_length=150,
    )

    short_course_name = models.CharField(
        "Nombre corto del curso",
        max_length=20,
    )

    topics = models.ForeignKey(
        CourseTopicsModel,
        verbose_name="Tema del curso",
        on_delete=models.CASCADE,
    )

    course_description = models.TextField(
        "Descripción del curso"
    )

    is_active = models.BooleanField(
        'Es un curso activo',
        default=True,
        help_text="Designa si el curso está activo",
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación del curso",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición del curso",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        db_table = 'apps_journal_groups_courses'
        ordering = ['order']

    def __str__(self) -> str:
        return self.course_name


class GroupsModel(models.Model):
    group_name = models.CharField(
        "Nombre del grupo",
        unique=True,
        max_length=150,
        help_text="Requerido. 150 carácteres o menos",
        error_messages={
            "único": "Este nombre de grupo ya existe",
            "requerido": "Debe ingresar un nombre de grupo",
        }
    )

    courses = models.ManyToManyField(
        CoursesModel,
        verbose_name="Cursos del grupo",
    )

    is_active = models.BooleanField(
        'Es un grupo activo',
        default=True,
        help_text="Designa si el grupo está activo",
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación del grupo",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición del grupo",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        db_table = 'apps_journal_groups_groups'
        ordering = ['order']

    def __str__(self) -> str:
        return self.group_name
