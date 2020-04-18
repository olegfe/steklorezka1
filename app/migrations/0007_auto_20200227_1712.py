# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-27 14:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200227_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 27, 17, 12, 26, 969018), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 2, 27, 17, 12, 26, 969018), verbose_name='Дата'),
        ),
    ]
