# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 13, 15, 26, 10, 388000, tzinfo=utc)),
        ),
    ]
