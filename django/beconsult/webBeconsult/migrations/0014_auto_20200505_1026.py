# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2020-05-05 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webBeconsult', '0013_auto_20200504_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='update',
            new_name='Actualizado',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='created',
            new_name='Creado',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='update',
            new_name='Actualizado',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='created',
            new_name='Creado',
        ),
        migrations.RenameField(
            model_name='joboffer',
            old_name='update',
            new_name='Actualizado',
        ),
        migrations.RenameField(
            model_name='joboffer',
            old_name='created',
            new_name='Creado',
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='Tags_en_Perfil',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
