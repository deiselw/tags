# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-03 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
