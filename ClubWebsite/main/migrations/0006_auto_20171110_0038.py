# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-09 19:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20171110_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 38, 15, 943499)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 38, 15, 943499)),
        ),
    ]