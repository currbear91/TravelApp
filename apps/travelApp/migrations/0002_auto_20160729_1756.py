# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(),
        ),
    ]
