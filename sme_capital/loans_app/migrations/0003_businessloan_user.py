# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-30 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans_app', '0002_auto_20170730_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessloan',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
