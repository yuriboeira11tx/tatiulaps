# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 18:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cidades', '0007_auto_20171020_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={},
        ),
        migrations.AlterModelManagers(
            name='cidade',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='cidade',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='cidade',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='nome',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='usuario',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
