# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20160104_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='submitter',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
