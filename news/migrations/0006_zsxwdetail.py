# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_type_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZSXWDetail',
            fields=[
                ('articleId', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, default='', blank=True)),
                ('date', models.CharField(max_length=255, default='')),
                ('author', models.CharField(max_length=255, default='')),
                ('deptname', models.CharField(max_length=255, default='')),
                ('videolink', models.CharField(max_length=255, default='')),
                ('content', models.CharField(max_length=4096, default='')),
            ],
            options={
                'ordering': ('-articleId',),
                'db_table': 'news_zsxw_detail',
            },
        ),
    ]
