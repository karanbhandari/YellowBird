# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20170121_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='location_x',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='query',
            name='location_y',
            field=models.FloatField(),
        ),
    ]
