# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-05 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20171003_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
