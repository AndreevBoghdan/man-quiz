# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_graphic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='answer',
            field=models.CharField(default='A', max_length=200),
        ),
    ]