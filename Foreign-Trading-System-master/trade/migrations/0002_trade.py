# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradeID', models.IntegerField()),
                ('commodityName', models.CharField(max_length=50)),
                ('importerName', models.CharField(max_length=50)),
                ('exporterName', models.CharField(max_length=50)),
                ('datePerformed', models.DateTimeField()),
                ('totalPrice', models.FloatField()),
            ],
        ),
    ]
