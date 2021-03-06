# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-30 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_team_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='height_field',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='width_field',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='picture',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='projects/', width_field='width_field'),
        ),
    ]
