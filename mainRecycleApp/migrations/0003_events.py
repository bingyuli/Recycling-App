# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainRecycleApp', '0002_specialwastesite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borough', models.TextField()),
                ('time', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
