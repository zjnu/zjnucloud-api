# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150915_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='link',
            field=models.CharField(default='', max_length=255),
        ),
    ]
