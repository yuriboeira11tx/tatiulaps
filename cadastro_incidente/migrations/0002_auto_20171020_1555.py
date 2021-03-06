# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_incidente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidente',
            name='tipo',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incidente',
            name='gravidade',
            field=models.CharField(choices=[('AC', 'Acidente'), ('DMP', 'Médio Porte'), ('DGP', 'Grande Porte'), ('DMGP', 'Muito Grande Porte')], max_length=4),
        ),
    ]
