# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2020-04-30 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webBeconsult', '0003_auto_20200430_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='/static/webBeconsult/img/uploads'),
        ),
    ]