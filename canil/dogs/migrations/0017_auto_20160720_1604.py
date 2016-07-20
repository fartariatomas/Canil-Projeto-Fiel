# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0016_auto_20160720_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(choices=[('Macho', 'Macho'), ('Femea', 'Femea')], max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='size',
            field=models.CharField(choices=[('Pequeno Porte', 'Pequeno Porte'), ('Medio Porte', 'Medio Porte'), ('Grande Porte', 'Grande Porte'), ('Muito Grande Porte', 'Muito Grande Porte')], max_length=20),
        ),
    ]
