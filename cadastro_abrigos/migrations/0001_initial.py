# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abrigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('rua', models.CharField(max_length=90)),
                ('bairro', models.CharField(max_length=30)),
                ('numero', models.IntegerField()),
                ('capacidade', models.IntegerField()),
            ],
        ),
    ]
