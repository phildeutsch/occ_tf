# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-31 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tf', '0034_auto_20160731_1937'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FifaMatch',
            new_name='FifaMatch_old',
        ),
        migrations.RemoveField(
            model_name='tfmatch_old',
            name='teams',
        ),
        migrations.DeleteModel(
            name='TfMatch_old',
        ),
    ]