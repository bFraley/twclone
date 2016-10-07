# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twapp', '0002_auto_20161003_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='memb',
            field=models.ForeignKey(to='twapp.Member', default=1),
            preserve_default=False,
        ),
    ]
