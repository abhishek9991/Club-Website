# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-21 17:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20171117_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dp',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time(22, 51, 2, 157725)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(22, 51, 2, 157725)),
        ),
    ]
