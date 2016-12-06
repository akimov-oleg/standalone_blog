# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата комментария')),
                ('text', models.TextField(blank=True, verbose_name='Текст комментария')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата публикации')),
                ('header', models.CharField(max_length=32, verbose_name='Заголовок публикации')),
                ('file_path', models.FilePathField(verbose_name='Путь к файлу публикации')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Post'),
        ),
    ]