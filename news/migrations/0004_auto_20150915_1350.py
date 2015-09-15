# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150915_1349'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Type',
        ),
        migrations.RenameModel(
            old_name='NewsZSXW',
            new_name='ZSXW',
        ),
    ]
