from django.utils import timezone

from django.db import models

from apps.authentication.users.models import PeopleModel

from apps.journal.groups.models import (
    GroupsModel,
    CoursesModel,
    CourseTopicsModel
)


class JournalModel(models.Model):
    teacher = models.ForeignKey(
        PeopleModel,
        on_delete=models.DO_NOTHING,
        verbose_name="Profesor",
    )

    group = models.ForeignKey(
        GroupsModel,
        on_delete=models.DO_NOTHING,
        verbose_name="Grupo (Ejm: 10A)",
    )

    course = models.ForeignKey(
        CoursesModel,
        on_delete=models.DO_NOTHING,
        verbose_name="Materia (Ejm: Matemáticas)",
    )
    
    topic = models.ForeignKey(
        CourseTopicsModel,
        on_delete=models.DO_NOTHING,
        verbose_name="Tema del curso (Ejm: Trigonometría)",
    )

    journal_date = models.DateField(
        "Fecha de registro del diario",
        default=timezone.now,
    )

    pedagogical_reflection = models.TextField(
        "Reflexión pedagógica",
        blank=True,
        null=True
    )

    observations = models.TextField(
        "Observaciones",
        blank=True,
        null=True
    )

    description = models.TextField(
        "Descripción",
        blank=True,
        null=True
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
