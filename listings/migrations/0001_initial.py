# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 06:52
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TNZImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.IntegerField()),
                ('unique_id', models.IntegerField()),
                ('type_o_id', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('label', models.TextField()),
                ('width', models.SmallIntegerField()),
                ('height', models.SmallIntegerField()),
                ('order', models.SmallIntegerField(blank=True, null=True)),
                ('market', models.CharField(max_length=5)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('asset_type', models.CharField(max_length=20)),
                ('credit', models.TextField()),
                ('exists', models.BooleanField()),
                ('caption', models.TextField(blank=True)),
                ('url', models.TextField()),
                ('file', models.ImageField(null=True, upload_to='listings/')),
            ],
        ),
        migrations.CreateModel(
            name='TNZListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('unique_id', models.IntegerField()),
                ('market', models.CharField(max_length=5)),
                ('modified_date', models.DateTimeField(null=True)),
                ('listing_description', models.TextField()),
                ('listing_summary', models.TextField()),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('regionname', models.CharField(max_length=50)),
                ('business_type', models.CharField(max_length=200)),
                ('minimum_age', models.SmallIntegerField(null=True)),
                ('max_capacity', models.TextField()),
                ('website_link', models.TextField()),
                ('booking_link', models.TextField()),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('operational_hours', models.TextField()),
                ('street', models.TextField()),
                ('suburb', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=50)),
                ('proximity_to_town', models.TextField()),
                ('proximity_to_airport', models.TextField()),
                ('freephone', models.CharField(max_length=50)),
                ('booking_email', models.CharField(max_length=50)),
                ('cancellation_policy', models.TextField()),
                ('parking', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(null=True)),
                ('listing_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), null=True, size=None)),
                ('logo_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo_image_listing', to='listings.TNZImage')),
                ('main_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_image_listing', to='listings.TNZImage')),
            ],
        ),
        migrations.CreateModel(
            name='TNZRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField()),
                ('o_id', models.IntegerField()),
                ('label', models.CharField(max_length=200)),
                ('name_key', models.CharField(max_length=50)),
                ('market', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TNZTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField()),
                ('o_id', models.IntegerField()),
                ('label', models.CharField(max_length=200)),
                ('listing_count', models.IntegerField()),
                ('name_key', models.CharField(max_length=200)),
                ('market', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='tnzlisting',
            name='tags',
            field=models.ManyToManyField(related_name='listings', to='listings.TNZTag'),
        ),
        migrations.AddField(
            model_name='tnzimage',
            name='gallery_image_listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='listings.TNZListing'),
        ),
    ]
