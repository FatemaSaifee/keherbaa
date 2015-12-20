# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0002_auto_20151220_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypeBlockPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.CharField(max_length=100)),
                ('productTypeBlock', models.ForeignKey(to='paints.ProductTypeBlock')),
            ],
        ),
        migrations.RemoveField(
            model_name='producttypeblockponit',
            name='productTypeBlock',
        ),
        migrations.DeleteModel(
            name='ProductTypeBlockPonit',
        ),
    ]
