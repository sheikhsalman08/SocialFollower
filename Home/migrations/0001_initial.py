# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(null=True, blank=True)),
                ('amount', models.IntegerField()),
                ('order_social_site', models.CharField(default=b'Did Not Put', max_length=230)),
                ('order_social_site_user_name', models.CharField(default=b'Did Not Put', max_length=30)),
                ('order_social_site_url', models.CharField(default=b'Did Not Put', max_length=30)),
                ('type', models.CharField(default=b'Did Not Put', max_length=230, choices=[('1', 'instagram'), ('2', 'facebook'), ('3', 'youtube')])),
                ('payment_status', models.BooleanField(default=False)),
                ('visibility_by_admin', models.NullBooleanField(default=True)),
                ('by_user', models.ForeignKey(related_name='owner', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
