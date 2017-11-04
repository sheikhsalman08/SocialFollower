# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-12 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_auto_20171011_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_social_site_url',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_social_site_user_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'instagram'), ('2', 'facebook'), ('3', 'youtube')], default='Did Not Put', max_length=230, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='visibility_by_admin',
            field=models.BooleanField(default=True),
        ),
    ]