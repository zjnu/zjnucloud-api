# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_zsxwdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='TZGG',
            fields=[
                ('articleId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
                ('overview', models.CharField(max_length=2048, default='', blank=True)),
                ('author', models.CharField(max_length=255, default='')),
                ('hits', models.CharField(max_length=255, default='')),
            ],
            options={
                'ordering': ('-articleId',),
                'db_table': 'news_tzgg',
            },
        ),
        migrations.CreateModel(
            name='TZGGDetail',
            fields=[
                ('articleId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
                ('author', models.CharField(max_length=255, default='')),
                ('deptname', models.CharField(max_length=255, default='')),
                ('content', models.CharField(max_length=4096, default='')),
            ],
            options={
                'ordering': ('-articleId',),
                'db_table': 'news_tzgg_detail',
            },
        ),
        migrations.CreateModel(
            name='XSDT',
            fields=[
                ('articleId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
                ('overview', models.CharField(max_length=2048, default='', blank=True)),
                ('author', models.CharField(max_length=255, default='')),
                ('hits', models.CharField(max_length=255, default='')),
            ],
            options={
                'ordering': ('-articleId',),
            },
        ),
        migrations.CreateModel(
            name='XSDTDetail',
            fields=[
                ('articleId', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
                ('author', models.CharField(max_length=255, default='')),
                ('deptname', models.CharField(max_length=255, default='')),
                ('videolink', models.CharField(max_length=255, default='')),
                ('content', models.CharField(max_length=4096, default='')),
            ],
            options={
                'ordering': ('-articleId',),
                'db_table': 'news_xsdt_detail',
            },
        ),
    ]
