# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeechDetail',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, default='')),
                ('date', models.CharField(max_length=16, default='')),
                ('content', models.CharField(max_length=255, default='')),
            ],
            options={
                'db_table': 'speech_detail',
                'ordering': ('-id',),
            },
        ),
    ]
