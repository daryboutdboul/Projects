# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(decimal_places=2, max_digits=4)),
                ('bid_size', models.IntegerField()),
                ('ask', models.DecimalField(decimal_places=2, max_digits=2)),
                ('ask_size', models.IntegerField()),
                ('login', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Paris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=2, max_digits=2)),
                ('login_buyer', models.CharField(max_length=10)),
                ('login_seller', models.CharField(max_length=10)),
                ('paris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Paris')),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='paris',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Paris'),
        ),
    ]
