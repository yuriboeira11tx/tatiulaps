# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cidades', '0006_auto_20171020_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gravidade', models.CharField(choices=[('Ac', 'Acidente'), ('DMP', 'Médio Porte'), ('DGP', 'Grande Porte'), ('DMGP', 'Muito Grande Porte')], max_length=4)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cidades.Cidade')),
            ],
        ),
    ]
