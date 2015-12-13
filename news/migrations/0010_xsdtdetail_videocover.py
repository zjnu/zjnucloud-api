# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_zsxwdetail_videocover'),
    ]

    operations = [
        migrations.AddField(
            model_name='xsdtdetail',
            name='videocover',
            field=models.CharField(max_length=255, default=''),
        ),
    ]
