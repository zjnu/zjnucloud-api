# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_tzgg_tzggdetail_xsdt_xsdtdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tzggdetail',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='xsdtdetail',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='zsxwdetail',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
