# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0002_remove_gametype_gametype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gametype',
            name='players',
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]
