# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-04 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(max_length=200),
        ),
    ]
