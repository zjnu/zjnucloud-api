# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('articleId', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(default='', max_length=255, blank=True)),
                ('overview', models.CharField(default='', max_length=2048, blank=True)),
                ('date', models.CharField(default='', max_length=255)),
                ('author', models.CharField(default='', max_length=255)),
                ('hits', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ('articleId',),
            },
        ),
    ]
