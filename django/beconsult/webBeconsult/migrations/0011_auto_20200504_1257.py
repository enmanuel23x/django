# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2020-05-04 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webBeconsult', '0010_auto_20200430_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='description',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='image',
            new_name='Imagen',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='title',
            new_name='Titulo',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='url',
            new_name='URL',
        ),
        migrations.RemoveField(
            model_name='joboffer',
            name='profile',
        ),
        migrations.AddField(
            model_name='joboffer',
            name='profile_tags',
            field=models.CharField(max_length=250, null=True),
        ),
    ]