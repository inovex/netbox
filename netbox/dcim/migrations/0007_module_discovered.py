# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0006_remove_device_ro_snmp'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='discovered',
            field=models.BooleanField(default=False, verbose_name=b'Discovered'),
        ),
    ]