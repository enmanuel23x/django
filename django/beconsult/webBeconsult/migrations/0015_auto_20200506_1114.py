# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2020-05-06 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webBeconsult', '0014_auto_20200505_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employees',
            name='Nombre',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Titulo',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='Titulo',
            field=models.CharField(max_length=120),
        ),
        migrations.AddField(
            model_name='joboffer',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webBeconsult.Data'),
        ),
    ]
