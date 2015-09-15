# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150913_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('category', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='NewsZSXW',
            fields=[
                ('articleId', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(default='', blank=True, max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('overview', models.CharField(default='', blank=True, max_length=2048)),
                ('author', models.CharField(default='', max_length=255)),
                ('hits', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ('-articleId',),
            },
        ),
        migrations.DeleteModel(
            name='zsxw',
        ),
    ]
