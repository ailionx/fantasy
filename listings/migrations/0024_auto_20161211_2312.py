# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 10:12
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_auto_20161211_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnzlisting',
            name='listing_types',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
