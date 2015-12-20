# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0003_auto_20151220_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttypeblock',
            name='description',
        ),
    ]
