# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-09 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_statistic'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='quiz_id',
            field=models.IntegerField(default=0),
        ),
    ]