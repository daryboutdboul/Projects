# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_paris_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='ask',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
