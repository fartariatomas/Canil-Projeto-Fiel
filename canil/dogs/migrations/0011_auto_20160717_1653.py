# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0010_auto_20160717_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='number',
            new_name='number_register',
        ),
    ]
