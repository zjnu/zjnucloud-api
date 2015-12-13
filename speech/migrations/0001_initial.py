# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('date', models.CharField(default='', max_length=16)),
                ('href', models.CharField(default='', max_length=255)),
                ('pic', models.CharField(default='', max_length=255)),
                ('overview', models.CharField(default='', max_length=2048)),
            ],
            options={
                'ordering': ('-id',),
                'db_table': 'speech',
            },
        ),
    ]
