# Generated by Django 4.0.5 on 2022-07-13 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_nameandlinkmodel_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nameandlinkmodel',
            name='icon',
            field=models.CharField(max_length=100, verbose_name="Icono que va dentro de la etiqueta <i class=''>"),
        ),
    ]
