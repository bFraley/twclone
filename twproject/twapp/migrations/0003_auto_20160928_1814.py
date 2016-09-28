# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twapp', '0002_auto_20160928_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='tweets',
        ),
        migrations.AddField(
            model_name='tweet',
            name='mem',
            field=models.ForeignKey(to='twapp.Member', null=True),
        ),
    ]
