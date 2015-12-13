# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speech', '0002_speechdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechdetail',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
