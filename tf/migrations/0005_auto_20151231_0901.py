# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tf', '0004_auto_20151230_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='tfplayer',
            name='full_name',
            field=models.CharField(default='dummyname', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tfplayer',
            name='grade',
            field=models.CharField(default='AC', max_length=2),
        ),
    ]
