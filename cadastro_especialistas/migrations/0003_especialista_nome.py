# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_especialistas', '0002_auto_20171020_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialista',
            name='nome',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
