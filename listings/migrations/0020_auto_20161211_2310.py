# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0019_auto_20161127_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnzlisting',
            name='latitude',
            field=models.FloatField(null=True),
        ),
    ]