# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-13 16:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20171113_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=datetime.time(21, 44, 21, 992372)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=datetime.time(21, 44, 21, 992372)),
        ),
    ]