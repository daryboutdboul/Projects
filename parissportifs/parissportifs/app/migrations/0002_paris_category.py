# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paris',
            name='category',
            field=models.CharField(default='sport', max_length=200),
            preserve_default=False,
        ),
    ]
