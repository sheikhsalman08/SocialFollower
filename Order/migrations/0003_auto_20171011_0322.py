# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20171010_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_social_site',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_social_site_url',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_social_site_user_name',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
