# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2020-05-04 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webBeconsult', '0012_auto_20200504_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='image',
            new_name='Imagen',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='name',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='joboffer',
            old_name='description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='joboffer',
            old_name='profile_tags',
            new_name='Tags_en_Perfil',
        ),
    ]