# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_remove_tnzlisting_raw_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tnzlisting',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
    ]