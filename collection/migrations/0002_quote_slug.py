# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-16 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='slug',
            field=models.SlugField(default='quote-1', unique=True),
        ),
    ]
