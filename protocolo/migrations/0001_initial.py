# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionProtocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clasificacion', models.CharField(default=b'Sin clasificacion', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=5000)),
                ('version', models.FloatField(default=1.0)),
                ('fecha_creacion', models.DateField(blank=True, default=datetime.datetime.now)),
                ('codigo', models.CharField(max_length=10)),
                ('observaciones', models.CharField(blank=True, max_length=500)),
                ('clasificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasificacion', to='protocolo.ClasificacionProtocolo')),
                ('insumos', models.ManyToManyField(related_name='insumos', to='insumo.Insumo')),
            ],
        ),
        migrations.AddField(
            model_name='paso',
            name='protocolo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protocolo.Protocolo'),
        ),
    ]
