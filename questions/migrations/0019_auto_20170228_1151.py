# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20170228_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
