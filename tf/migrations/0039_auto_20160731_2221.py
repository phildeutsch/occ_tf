# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-31 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tf', '0038_auto_20160731_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='team1_elos',
            field=models.CharField(default='0 0', max_length=9),
        ),
        migrations.AddField(
            model_name='match',
            name='team2_elos',
            field=models.CharField(default='0 0', max_length=9),
        ),
    ]
