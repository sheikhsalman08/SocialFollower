# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='visibility_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]
