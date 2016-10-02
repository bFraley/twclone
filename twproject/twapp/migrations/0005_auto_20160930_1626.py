# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twapp', '0004_auto_20160929_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['username']},
        ),
    ]
