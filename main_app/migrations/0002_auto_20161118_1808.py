# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file_path',
        ),
        migrations.AddField(
            model_name='post',
            name='post_text',
            field=models.TextField(blank=True, verbose_name='Содержимое публикации'),
        ),
    ]