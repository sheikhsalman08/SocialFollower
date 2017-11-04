# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_auto_20171011_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_social_site_url',
            field=models.CharField(default=b'', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_social_site_user_name',
            field=models.CharField(default=b'', max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(default=b'Did Not Put', max_length=230, null=True, blank=True, choices=[('1', 'instagram'), ('2', 'facebook'), ('3', 'youtube')]),
        ),
    ]
