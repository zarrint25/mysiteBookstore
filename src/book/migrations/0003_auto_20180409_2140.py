# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-09 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180409_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=200),
        ),
    ]