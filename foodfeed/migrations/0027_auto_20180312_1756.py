# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 17:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0026_auto_20180312_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 12, 17, 56, 37, 86642)),
        ),
    ]
