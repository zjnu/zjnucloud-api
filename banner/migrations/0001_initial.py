# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, max_length=11)),
                ('image', models.CharField(max_length=255)),
                ('href', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'banner',
            },
        ),
    ]
