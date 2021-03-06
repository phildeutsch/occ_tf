# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-03 09:30
from __future__ import unicode_literals

from django.db import migrations

def migrate_players(apps, schema_editor):
    Teams = apps.get_model("tf", "TfTeam")
    for t in Teams.objects.all():
        t.players.add(t.player2)
        if not t.is_single_player:
            t.players.add(t.player1)
        t.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tf', '0013_tfteam_players'),
    ]

    operations = [
        migrations.RunPython(migrate_players),
    ]
