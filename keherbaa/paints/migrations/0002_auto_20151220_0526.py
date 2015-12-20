# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypeBlockPonit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('point', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='producttypeblock',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AddField(
            model_name='producttypeblockponit',
            name='productTypeBlock',
            field=models.ForeignKey(to='paints.ProductTypeBlock'),
        ),
    ]
