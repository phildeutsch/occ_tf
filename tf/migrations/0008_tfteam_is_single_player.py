# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tf', '0007_auto_20160109_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='tfteam',
            name='is_single_player',
            field=models.BooleanField(default=False),
        ),
    ]
