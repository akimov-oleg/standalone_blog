# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 17:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_comment_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Дата комментария'),
        ),
    ]
