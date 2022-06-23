from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

# reto crear un modelo para registrar meta tags
# las meta tags estan conformadas de la siguiente manera:
# type="name" content="content"
"""
<meta name="title" content="Journal App" />
<meta name="description" content="Una breve pero cautivadora descripción de la app o de la página" />
<meta name="keywords" content="python, django, journalapp" />
<meta property="og.type" content="website" />
<meta property="og:url" content="{{ url_base }}" />
<meta property="og:title" content="Journal App" />
<meta property="og:description" content="Una breve pero cautivadora descripción de la app o de la página" />
""" 

class LogoModel(models.Model):
    title = models.CharField(
        "Título",
        max_length=100
    )

    logo_light = models.ImageField(
        "Logo modo luz",
        upload_to='general/logo/light'
    )

    logo_dark = models.ImageField(
        "Logo modo oscuro",
        upload_to='general/logo/dark'
    )

    favicon = models.ImageField(
        "Favicon",
        upload_to='general/favicon'
    )

    is_active = models.BooleanField(
        'Se va a mostrar este logo?',
        default=True,
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    class Meta:
        verbose_name = 'Logos'
        verbose_name_plural = 'Logos'
        db_table = 'apps_home_logos'
        ordering = ['order']


class StartDescriptionModel(models.Model):
    description = RichTextField(
        "Título del inicio",
    )

    is_active = models.BooleanField(
        'Esta activo?',
        default=True,
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    class Meta:
        verbose_name = 'Título del inicio'
        verbose_name_plural = 'Título del inicio'
        db_table = 'apps_home_title_index'
        ordering = ['order']


class ContentIndexModel(models.Model):
    description = RichTextField(
        "Contenido de la página principal",
    )

    is_active = models.BooleanField(
        'Esta activa?',
        default=True,
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        help_text="Fecha de creación",
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        help_text="Fecha de edición",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
    )

    class Meta:
        verbose_name = 'Contenido principal'
        verbose_name_plural = 'Contenido principal'
        db_table = 'apps_home_content_index'
        ordering = ['order']
        