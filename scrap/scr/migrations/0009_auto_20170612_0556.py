# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-12 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scr', '0008_category_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Random_m',
        ),
        migrations.AddField(
            model_name='quote',
            name='certificates',
            field=models.URLField(default='null'),
        ),
        migrations.AddField(
            model_name='quote',
            name='time',
            field=models.CharField(default='12/06/17', max_length=20),
        ),
    ]
