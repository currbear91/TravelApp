# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0006_auto_20160727_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(null=True, upload_to='media/TravelApp'),
        ),
    ]
