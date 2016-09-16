# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_xsdtdetail_videocover'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChuYang',
            fields=[
                ('articleId', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
            ],
            options={
                'ordering': ('-articleId',),
                'db_table': 'news_chuyang',
            },
        ),
        migrations.CreateModel(
            name='ChuYangDetail',
            fields=[
                ('articleId', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
                ('author', models.CharField(max_length=255, default='')),
                ('content', models.TextField(default='')),
            ],
            options={
                'ordering': ('-articleId',),
                'db_table': 'news_chuyang_detail',
            },
        ),
    ]
