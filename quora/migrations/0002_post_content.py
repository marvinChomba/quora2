# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-22 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='Nothing'),
            preserve_default=False,
        ),
    ]
