# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_remove_survey_contentname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': ' Answer'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': '  Question'},
        ),
        migrations.AlterModelOptions(
            name='statistic',
            options={'verbose_name_plural': 'Statistic'},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'verbose_name_plural': '   Survey'},
        ),
    ]
