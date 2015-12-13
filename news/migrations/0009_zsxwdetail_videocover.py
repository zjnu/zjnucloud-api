# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20151018_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='zsxwdetail',
            name='videocover',
            field=models.CharField(max_length=255, default=''),
        ),
    ]
