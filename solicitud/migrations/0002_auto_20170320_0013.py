# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='asistente',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='titulo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]