# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20170204_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]