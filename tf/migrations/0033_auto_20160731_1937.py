# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-31 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tf', '0032_migrate_tfmatches'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TfMatch',
            new_name='TfMatch_old',
        ),
    ]
